import io
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageFont
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

url_font = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial.ttf?raw=True'
normal_font = io.BytesIO(urlopen(url_font).read())

url_bold = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial_Bold.ttf?raw=True'
bold_font = io.BytesIO(urlopen(url_bold).read())


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
            duration = activity.end_date

            # Converta o timestamp em um objeto datetime
            dt = datetime.datetime.fromtimestamp(timestamp).astimezone(gmt3_tz)

            # Obtenha as partes do dia e do mês em formato de texto
            day = str(dt.day)
            month = MONTH_DICT[
                dt.month].title()  # %B retorna o mês em formato de texto completo, capitalize para capitalizar a primeira letra

            # Obtenha o ano, hora e minuto em formato de texto
            year = str(dt.year)
            hour = dt.strftime("%H:%M")

            # Combine as partes em um único texto
            text_date = f"{day} de {month} de {year}"
            duration_text = get_time(duration)

            # Imprima o resultado
            # print(text_date)
            # print(duration_text)

            firstBlockA = 'O'
            firstBlockB = 'Instituto Mauá de Tecnologia confere'
            firstBlockC = 'a'

            secondBlock = name

            thirdBlock_a = "o presente certificado, por ter participado da atividade:"
            thirdBlock_b = title
            ThirdBlock_c1 = "realizada no dia "
            ThirdBlock_c2 = text_date
            ThirdBlock_c3 = "na"
            ThirdBlock_d = "Semana Mauá de Inovação e Liderança e Empreendedorismo,"
            ThirdBlock_e1 = "com duração de "
            ThirdBlock_e2 = duration_text

            FourthBlock = "São Caetano do Sul, 27 de maio de 2023."

            # fontes e fontsize a serem definidos
            normal_font.seek(0)
            firstFont = ImageFont.truetype(normal_font, 40)

            bold_font.seek(0)
            firstFontbd = ImageFont.truetype(bold_font, 40)

            bold_font.seek(0)
            secondFont = ImageFont.truetype(bold_font, 60)

            normal_font.seek(0)
            thirdFont = ImageFont.truetype(normal_font, 40)

            bold_font.seek(0)
            thirdFontbd = ImageFont.truetype(bold_font, 40)

            normal_font.seek(0)
            fourthFont = ImageFont.truetype(normal_font, 40)

            # diretório "geral" / não-relativo
            img = Image.open(io.BytesIO(template_file))
            draw = ImageDraw.Draw(img)

            # Largura e altura do certificado
            W, H = (2667, 1300)
            spc = 7

            # obs: y=0 é a altura no meio da imagem
            # Capturar largura e altura do primeiro bloco de texto
            # espaçamento do espaço é spc = 4

            _, _, w, h = draw.textbbox((0, 550), firstBlockA, font=firstFont)
            w1 = w + spc
            _, _, w, h = draw.textbbox((0, 550), firstBlockB, font=firstFontbd)
            w2 = w1 + w + spc
            _, _, w, h = draw.textbbox((0, 550), firstBlockC, font=firstFont)
            w3 = w2 + w

            # coeficiente k de disposição dos textos ao longo do eixo y:

            yk = H / 646

            # plotar primeiro bloco de texto
            # alteração pra /3 pra aumentar o espaçamento
            draw.text(((W - w3) / 2, ((H - h) / 2.5)), firstBlockA, font=firstFont, fill='black')
            draw.text((((W - w3) / 2) + w1, (H - h) / 2.5), firstBlockB, font=firstFontbd, fill='black')
            draw.text((((W - w3) / 2) + w2, (H - h) / 2.5), firstBlockC, font=firstFont, fill='black')

            # Capturar largura e altura do primeiro bloco de texto
            _, _, w, h = draw.textbbox((0, 80 * yk), secondBlock, font=secondFont)
            # plotar primeiro bloco de texto
            draw.text(((W - w) / 2, (H - h) / 2 - 50), secondBlock, font=secondFont, fill='black')

            # Capturar largura e altura do primeiro bloco de texto
            _, _, w, h = draw.textbbox((5, -68 * yk), thirdBlock_a, font=thirdFont)
            # plotar primeiro bloco de texto
            draw.text(((W - w) / 2, (H - h) / 2), thirdBlock_a, font=thirdFont, fill='black')

            # Capturar largura e altura do primeiro bloco de texto
            _, _, w, h = draw.textbbox((0, (-110) * yk), thirdBlock_b, font=thirdFontbd)
            # plotar primeiro bloco de texto
            draw.text(((W - w) / 2, (H - h) / 2), thirdBlock_b, font=thirdFontbd, fill='black')
            h_terceira_linha = (H - h) / 2

            # "realizado no dia + {dia}"

            _, _, w, h = draw.textbbox((0, 300), ThirdBlock_c1, font=thirdFont)
            w1 = w + spc
            _, _, w, h = draw.textbbox((0, 300), ThirdBlock_c2, font=thirdFontbd)
            w2 = w1 + w + spc
            _, _, w, h = draw.textbbox((0, 300), ThirdBlock_c3, font=thirdFontbd)
            w2 = w + w2

            draw.text(((W - w3) / 2, (h_terceira_linha + 44)), ThirdBlock_c1, font=thirdFont, fill='black')
            draw.text((((W - w3) / 2) + w1, (h_terceira_linha + 44)), ThirdBlock_c2, font=thirdFontbd, fill='black')
            draw.text((((W - w3) / 2) + w2 - w + spc, (h_terceira_linha + 44)), ThirdBlock_c3, font=thirdFont,
                      fill='black')

            _, _, w, h = draw.textbbox((0, (-200) * yk), ThirdBlock_d, font=thirdFontbd)
            # plotar primeiro bloco de texto
            draw.text(((W - w) / 2, (H - h) / 2), ThirdBlock_d, font=thirdFontbd, fill='black')

            # "com duração de + {duracao}"
            _, _, w, h = draw.textbbox((0, 300), ThirdBlock_e1, font=thirdFont)
            w1 = w + spc
            _, _, w, h = draw.textbbox((0, 300), ThirdBlock_e2, font=thirdFontbd)
            w2 = w1 + w

            draw.text(((W - w2) / 2, (h_terceira_linha + 132)), ThirdBlock_e1, font=thirdFont, fill='black')
            draw.text((((W - w2) / 2) + w1, (h_terceira_linha + 132)), ThirdBlock_e2, font=thirdFontbd, fill='black')

            # Capturar largura e altura do primeiro bloco de texto
            _, _, w, h = draw.textbbox((0, -280 * yk), FourthBlock, font=fourthFont)
            # plotar primeiro bloco de texto
            draw.text(((W - w) / 2, (H - h) / 1.8), FourthBlock, font=fourthFont, fill='black')

            output_pdf = io.BytesIO()

            img.save(output_pdf, format='PDF')

            hash_value = hashlib.sha256((email + hash_key + activity_code).encode('utf-8')).hexdigest()[0:5]

            # Set the filename for the generated certificate
            output_filename = f"{activity_code}_{email.split('@')[0]}_{hash_value}.pdf"
            print(output_filename)

            # Write the output PDF to a file
            output_pdf_content = output_pdf.getvalue()

            hash_name = hashlib.sha256((email + hash_key).encode('utf-8')).hexdigest()

            s3.Object(bucket_name, f"{hash_name}/{output_filename}").put(Body=output_pdf_content)

    except Exception as e:
        print(F"ERRO {activity.code}: ", e)


def lambda_handler(event, context):
    bucket_name = os.environ["BUCKET_NAME"]

    file_name = "CERTIFICATE_TEMPLATE"

    template_name = hashlib.sha256((file_name + hash_key).encode('utf-8')).hexdigest() + '.png'
    print("template_name = ", template_name)
    file_obj = s3.Object(bucket_name, template_name)
    file_content = file_obj.get()['Body'].read()

    activities_with_enrollments = repo_activity.get_all_activities_admin()
    activities_with_enrollments.sort(key=lambda a: a[0].start_date)

    user_id_list = list()

    for activity, enrollments in activities_with_enrollments:
        user_id_list.extend(
            [enrollment.user_id for enrollment in enrollments if enrollment.state == ENROLLMENT_STATE.COMPLETED])

    set_user_id_list = set(user_id_list)

    users = repo_user.get_users_info(list(set_user_id_list))

    users_dict = {user.user_id: user for user in users}

    for activity, enrollments in activities_with_enrollments:
        file_content = file_obj.get()['Body'].read()
        users = [users_dict.get(enrollment.user_id, "NOT_FOUND") for enrollment in enrollments if
                 enrollment.state == ENROLLMENT_STATE.COMPLETED]

        generate_certificate(activity=activity, users=users, template_file=file_content, bucket_name=bucket_name)

