import io
import PyPDF2
from reportlab.pdfgen import canvas
import datetime 
from src.shared.environments import Environments
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
import boto3
import os
import hashlib

repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()
hash_key = os.environ.get("HASH_KEY")
    
def get_time(minutes: int):
    if minutes < 60:
        if minutes == 1:
            return f"{minutes} minuto"
        else:
            return f"{minutes} minutos"
    else:
        hours = minutes // 60
        minutes = minutes % 60
        if hours == 1:
            return f"{hours} hora" + (f" e {minutes} minutos" if minutes != 0 else "")
        else:
            return f"{hours} horas" + (f" e {minutes} minutos" if minutes != 0 else "")

s3 = boto3.resource('s3')


def generate_certificate(bucket_name: str, activity: Activity, template_file, users):
    try:
        for user in users:
            if not type(user) == UserInfo:
                continue
            
            name = user.name
            social_name = user.social_name
            
            if user.certificate_with_social_name and social_name:
                name = social_name

            MONTH_DICT = {
                1: "janeiro",
                2: "fevereiro",
                3: "março",
                4: "abril",
                5: "maio",
                6: "junho",
                7: "julho",
                8: "agosto",
                9: "setembro",
                10: "outubro",
                11: "novembro",
                12: "dezembro"
            }
            
            gmt3_tz = datetime.timezone(datetime.timedelta(hours=-3))  
            
            # Activity data
            
            title = activity.title
            activity_code = activity.code
            email = user.email
            
            # Defina o timestamp
            timestamp = activity.start_date / 1000  # dividido por 1000 para obter o valor em segundos
            duration = activity.duration
            
            # Converta o timestamp em um objeto datetime
            dt = datetime.datetime.fromtimestamp(timestamp).astimezone(gmt3_tz)
            
            # Obtenha as partes do dia e do mês em formato de texto
            day = str(dt.day)
            month = MONTH_DICT[dt.month].title()  # %B retorna o mês em formato de texto completo, capitalize para capitalizar a primeira letra
            
            # Obtenha o ano, hora e minuto em formato de texto
            year = str(dt.year)
            hour = dt.strftime("%H:%M")
            
            # Combine as partes em um único texto
            text_date = f"{day} de {month} de {year}"
            duration_text = get_time(duration)
            
            # Imprima o resultado
            # print(text_date)
            # print(duration_text)
            
            text = f"""o presente certificado, por ter participado na atividade
            {activity_code} - {title}
            realizada no dia {text_date} na
            Semana Mauá de Inovação, Liderança e Empreendedorismo 2023,
            com duração de {duration_text}.
            
            São Caetano do Sul, 19 de Março de 2023."""
            
            text_split = text.split("\n")
            
            print(text_split)
            
            hash_value = hashlib.sha256((email + hash_key + activity_code).encode('utf-8')).hexdigest()[0:5]

            # Set the filename for the generated certificate
            output_filename = f"{activity_code}_{email.split('@')[0]}_{hash_value}.pdf"
            print(output_filename)
            
            # # Load the certificate template PDF

            # Create a PDF reader object
            reader = PyPDF2.PdfReader(io.BytesIO(template_file))

            # Get the first page of the PDF
            page = reader.pages[0]

            # Get the width and height of the page
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)

            # Create a new PDF in memory
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=(width, height))

            # Add the text to the canvas
            can.setFont('Helvetica-Bold', 28)
            can.drawCentredString(width*0.55, height*0.6, name)

            height_description = height*0.5
            space = height*0.025

            can.setFont('Helvetica', 12)
            can.drawCentredString(width*0.55, height_description, text_split[0])

            height_description -= space

            can.setFont('Helvetica-Bold', 12)
            can.drawCentredString(width*0.55, height_description, text_split[1])

            height_description -= space

            can.setFont('Helvetica', 12)
            can.drawCentredString(width*0.55, height_description, text_split[2])

            height_description -= space
            
            can.setFont('Helvetica-Bold', 12)
            can.drawCentredString(width*0.55, height_description, text_split[3])
            
            height_description -= space
            
            can.setFont('Helvetica', 12)
            can.drawCentredString(width*0.55, height_description, text_split[4])
            
            height_description -= space
            
            can.setFont('Helvetica', 12)
            can.drawCentredString(width*0.55, height_description, text_split[5])
            
            height_description -= space

            can.setFont('Helvetica', 12)
            can.drawCentredString(width*0.55, height_description, text_split[6])
            
            can.save()    

            # Move to the beginning of the StringIO buffer
            packet.seek(0)

            # Create a PDF writer object
            writer = PyPDF2.PdfWriter()

            # Merge the original PDF with the new PDF
            overlay = PyPDF2.PdfReader(packet)
            page.merge_page (overlay.pages[0])
            writer.add_page(page)

            # Write the output PDF to a file
            output_pdf = io.BytesIO()
            
            writer.write(output_pdf)
            
            output_pdf_content = output_pdf.getvalue()

            hash_name = hashlib.sha256((email + hash_key).encode('utf-8')).hexdigest()
            
            s3.Object(bucket_name, f"{hash_name}/{output_filename}").put(Body=output_pdf_content)

    except Exception as e:
        print(F"ERRO {activity.code}: ", e)


def lambda_handler(event, context):
    
    bucket_name = os.environ["BUCKET_NAME"]

    file_obj = s3.Object(bucket_name, "CERTIFICATE_TEMPLATE.pdf")
    file_content = file_obj.get()['Body'].read()

    activities_with_enrollments = repo_activity.get_all_activities_admin()
    activities_with_enrollments.sort(key=lambda a: a[0].start_date)

    user_id_list = list()

    for activity, enrollments in activities_with_enrollments:
        user_id_list.extend([enrollment.user_id for enrollment in enrollments if enrollment.state == ENROLLMENT_STATE.COMPLETED])

    set_user_id_list = set(user_id_list)

    users = repo_user.get_users_info(list(set_user_id_list))

    users_dict = {user.user_id: user for user in users}

    for activity, enrollments in activities_with_enrollments:
        file_content = file_obj.get()['Body'].read()
        users = [users_dict.get(enrollment.user_id, "NOT_FOUND") for enrollment in enrollments if enrollment.state == ENROLLMENT_STATE.COMPLETED]

        generate_certificate(activity=activity, users=users, template_file=file_content, bucket_name=bucket_name)
