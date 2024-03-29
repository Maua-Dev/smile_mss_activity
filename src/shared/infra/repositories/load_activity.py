import time
from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.environments import Environments
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class LoadActivityRepositoryMock:
    activities = List[Activity]

    def __init__(self) -> None:
        self.activities = [
            Activity(
                code="ECM2345",
                title="Inovação e Tecnologia para o Futuro",
                description="A atividade trará uma discussão sobre as tendências da tecnologia e sua relação com o futuro. O objetivo é discutir como a inovação pode ser aplicada em diferentes áreas para resolver problemas do futuro, como mudanças climáticas, saúde, economia e sociedade. Serão apresentadas diversas perspectivas sobre o assunto, abrangendo desde a tecnologia em si até a cultura de inovação.",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1680650366000, #Tue Apr 04 2023 23:19:26 GMT+0000
                end_date=1680657566000,
                link=None,
                place="H332",
                responsible_professors=[User(name="Carol Santarelli", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[
                    Speaker(name="João Silva", bio="João Silva é o fundador e CEO da Tech Innovate, uma empresa de tecnologia que cria soluções inovadoras para problemas complexos. Ele tem mais de 20 anos de experiência em liderança empresarial e tecnologia. João já foi palestrante em diversas conferências e é reconhecido como uma das principais autoridades em inovação no Brasil.", company="Tech Innovate")
                ],
                total_slots=4,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1680447600000, #Sun Apr 02 2023 15:00:00 GMT+0000
                confirmation_code=None
            ),
            Activity(
                code="ELET355",
                title="TechArt: Explorando a Interação entre Tecnologia e Arte",
                description="A atividade TechArt é uma experiência única que explora a interação entre a tecnologia e a arte, mostrando como a tecnologia pode ser usada para criar e transformar a arte. Os participantes terão a oportunidade de ver e interagir com diferentes instalações artísticas que utilizam tecnologias como realidade aumentada, inteligência artificial e robótica. A atividade é aberta a todos os estudantes e profissionais da área de tecnologia e engenharia que têm interesse em explorar a relação entre a tecnologia e a arte.",
                activity_type=ACTIVITY_TYPE.CULTURAL_ACTIVITY,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1678663166000, #Sun Mar 12 2023 23:19:26 GMT+0000
                end_date=1678670366000,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name="Joana Silva", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Pedro Alves", bio="Desenvolvedor de software na TechArt Inc., Pedro é responsável por criar as soluções tecnológicas que permitem a interação dos participantes com as instalações artísticas. Ele tem formação em Ciência da Computação e é apaixonado por arte e tecnologia.", company="TechArt")],
                total_slots=10,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="COD1468",
                title="Exposição de arte contemporânea",
                description="Nesta visita técnica, os participantes terão a oportunidade de conhecer de perto a produção de automóveis elétricos, desde a montagem do chassi até a instalação dos sistemas eletrônicos. Além disso, serão apresentadas as tecnologias utilizadas na fabricação desses veículos, como motores elétricos, baterias de alta capacidade e sistemas de recarga.",
                activity_type=ACTIVITY_TYPE.TECHNICAL_VISITS,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1679440766000, #Tue Mar 21 2023 23:19:26 GMT+0000
                end_date=1679455166000,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Maria Luiza", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Rafaela Oliveira ", bio="Rafaela Oliveira é engenheira de materiais e atua na área de pesquisa e desenvolvimento da empresa DEF, fornecedora de peças para a indústria automotiva. Ela possui experiência na fabricação de materiais avançados utilizados em carros elétricos, como ligas de alumínio e polímeros de alta resistência.", company="Samsung")],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="HACKA355",
                title="Hackathon de Desenvolvimento de Software",
                description="O Hackathon de Desenvolvimento de Software é um evento que reunirá estudantes de engenharia e tecnologia para competir em equipes na criação de soluções de software inovadoras. Os participantes terão a oportunidade de trabalhar em projetos desafiadores, aprender novas habilidades e se conectar com profissionais do setor.",
                activity_type=ACTIVITY_TYPE.HACKATHON,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1682896766000, #Sun Apr 30 2023 23:19:26 GMT+0000
                end_date=1682929166000,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Carol Santarelli", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="Ana Silva", bio="Ana Silva é diretora de tecnologia na empresa ABC, onde lidera a equipe de desenvolvimento de software. Ela possui mais de 15 anos de experiência em tecnologia, tendo trabalhado em empresas como Microsoft e Google.", company="Apple"),
                          Speaker(name="Pedro Oliveira", bio="Professor de engenharia de software na universidade XYZ. Ele é um especialista em metodologias ágeis de desenvolvimento de software e tem sido um mentor de sucesso em hackathons anteriores.", company="Microsoft"),
                          Speaker(name="Maria Santos ", bio="Gerente de produto na empresa DEF, onde lidera a equipe de desenvolvimento de novos produtos. Ela é uma especialista em UX/UI design e tem trabalhado em projetos inovadores na área de tecnologia.", company="Samsung")],
                total_slots=15,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1682434800000, #Tue Apr 25 2023 15:00:00 GMT+0000
                confirmation_code=None
            ),
            Activity(
                code="LECT1231",
                title="Tendências em tecnologia e engenharia",
                description="Esta palestra apresentará as tendências mais recentes em tecnologia e engenharia, abordando desde a evolução das linguagens de programação até as novidades em inteligência artificial e robótica. Será uma excelente oportunidade para atualizar-se sobre as mais recentes inovações em áreas tão importantes para a economia mundial.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1683229161000, #Thu May 04 2023 19:39:21 GMT+0000
                end_date=1683236361000,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Maria Luiza", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Lucas Rodrigues", bio="Lucas Rodrigues é diretor de engenharia na empresa Big Tech, uma das líderes mundiais em tecnologia. Ele possui mais de 20 anos de experiência em engenharia de software e liderança de equipes de desenvolvimento, tendo trabalhado em empresas como Microsoft e Google.", company="Big Tech,")],
                total_slots=15,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="ECM251",
                title="Tecnologias emergentes para a indústria 4.0",
                description="Nesta palestra, especialistas em tecnologia e engenharia discutirão as tecnologias emergentes que estão impulsionando a transformação da indústria 4.0. Serão abordados tópicos como inteligência artificial, internet das coisas, computação em nuvem e realidade virtual, além de exemplos práticos de aplicação dessas tecnologias em diversos setores.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1682428766000,#Tue Apr 25 2023 13:19:26 GMT+0000
                end_date=1682435966000,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name="Maria Luiza", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Marcos Oliveira", bio="Diretor de tecnologia na empresa DEF, onde lidera a equipe responsável pelo desenvolvimento de soluções de internet das coisas para a indústria. Ele possui mais de 20 anos de experiência em tecnologia e engenharia, tendo trabalhado em empresas como Intel e Cisco.", company="DEF")],
                total_slots=20,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="SC456",
                title="Inovação em tecnologia e engenharia: desafios e oportunidades",
                description="Descrição: Nesta palestra, especialistas de renome no setor de tecnologia e engenharia irão discutir os desafios e oportunidades que surgem com as novas tecnologias e inovações em engenharia. Os palestrantes irão explorar tópicos como inteligência artificial, robótica, IoT, realidade aumentada e virtual, e como eles estão impactando o setor de tecnologia e engenharia.",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1682601566000, #Thu Apr 27 2023 13:19:26 GMT+0000
                end_date=1682606366000,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Carol Santarelli", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="ECM2312",
                title="Tecnologias disruptivas e o futuro da engenharia",
                description="Nesta palestra, serão apresentadas as principais tendências e tecnologias disruptivas que estão moldando o futuro da engenharia. Serão discutidos tópicos como inteligência artificial, internet das coisas, realidade virtual e aumentada, além das possibilidades de aplicação dessas tecnologias em diferentes setores da indústria.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1679923166000, #Mon Mar 27 2023 13:19:26 GMT+0000
                end_date=1680021966000,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Maria Luiza", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Ana Santos", bio="Ana Santos é especialista em inteligência artificial e inovação na indústria de engenharia. Ela trabalha na empresa DEF, onde lidera a equipe de pesquisa e desenvolvimento em inteligência artificial. Possui mais de 10 anos de experiência em pesquisa e desenvolvimento em inteligência artificial, tendo trabalhado em projetos inovadores em empresas como IBM e Microsoft.", company="DEF")],
                total_slots=2,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="ECM3212",
                title="Atividade da CODE",
                description="O Hackathon de Tecnologia e Engenharia é um evento em que equipes multidisciplinares terão a oportunidade de criar soluções inovadoras para desafios reais da indústria de tecnologia e engenharia. O objetivo é fomentar a criatividade, o trabalho em equipe e o desenvolvimento de habilidades técnicas e de negócios.",
                activity_type=ACTIVITY_TYPE.HACKATHON,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1679833166000, #Sun Mar 26 2023 12:19:26 GMT+0000
                end_date=1680212766000,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name= "Carol Santarelli", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="José Silva", bio="José é gerente de produto na empresa XYZ, uma grande empresa de tecnologia com atuação global. Ela possui mais de 15 anos de experiência em desenvolvimento de produtos e gestão de equipes, tendo liderado projetos de sucesso em diversas áreas da empresa.", company="XYZ")],
                total_slots=50,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="PRF246",
                title="Palestras de Tecnologia e Engenharia",
                description="As Palestras de Tecnologia e Engenharia são uma série de apresentações com os principais líderes e especialistas em tecnologia e engenharia do mercado. As palestras vão abranger diversos tópicos, incluindo inteligência artificial, internet das coisas, segurança cibernética, cloud computing, blockchain e muito mais. Os participantes terão a oportunidade de se inspirar e aprender com as histórias de sucesso desses profissionais de renome e ainda terão a chance de fazer perguntas no final.",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1681384766000, #Thu Apr 13 2023 11:19:26 GMT+0000
                end_date=1681393166000,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Carol Santarelli", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="Maria Santos", bio="Maria Santos é diretora de engenharia da empresa SkyTech, onde lidera a equipe de engenheiros de software responsáveis por desenvolver soluções em nuvem. Ela tem mais de 15 anos de experiência em engenharia de software, tendo trabalhado em empresas como Amazon e Oracle.", company="SkyTech")],
                total_slots=50,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="2468",
                title="Campeonato de Futebol Interdepartamental",
                description="O Campeonato de Futebol Interdepartamental é um evento esportivo que tem como objetivo promover a integração entre os funcionários da empresa. O campeonato será realizado durante os finais de semana, com jogos entre os departamentos da empresa. Os jogos serão realizados em um campo de futebol de grama sintética, com arbitragem profissional e placares eletrônicos. Além de incentivar a prática esportiva, o campeonato também irá promover a competição saudável e a camaradagem entre os colegas de trabalho.",
                activity_type=ACTIVITY_TYPE.SPORTS_ACTIVITY,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1681729200000, #Mon Apr 17 2023 11:00:00 GMT+0000
                end_date=1681740800000,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name="Carol Santarelli", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="José Silva", bio="João é gerente de recursos humanos da empresa TechPlay, onde lidera a equipe responsável pelo recrutamento, seleção e desenvolvimento de talentos. Além disso, Pedro é um ávido jogador de futebol e está ansioso para organizar este campeonato interdepartamental.", company="TechPlay")],
                total_slots=25,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="CAFE1231",
                title="Encontro de Ex-Alunos: Tecnologia e Carreira",
                description="O Encontro de Ex-Alunos: Tecnologia e Carreira é um evento organizado pela empresa TechPlay, com o objetivo de reunir ex-alunos da instituição para discutir temas relacionados à tecnologia e ao mercado de trabalho. Durante o evento, os participantes terão a oportunidade de compartilhar suas experiências e aprendizados, trocar ideias e fazer networking.",
                activity_type=ACTIVITY_TYPE.ALUMNI_CAFE,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1681740000000, #Mon Apr 17 2023 14:00:00 GMT+0000
                end_date=1681742700000,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Carol Santarelli", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="João Silva", bio=" ex-aluno da TechPlay e atualmente é líder técnico em uma startup de tecnologia. Ele irá compartilhar sua experiência em trabalhar em empresas de diferentes tamanhos e setores, falar sobre os desafios e oportunidades de trabalhar em uma startup e responder às perguntas dos participantes.", company="TechPlay")],
                total_slots=3,
                taken_slots=3,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1681311600000, #Wed Apr 12 2023 15:00:00 GMT+0000
                confirmation_code="555666"
            ),
            Activity(
                code="PINOQ1",
                title="Palestra sobre Intercâmbio na Faculdade",
                description="A Palestra sobre Intercâmbio na Faculdade é um evento que tem como objetivo informar os estudantes universitários sobre as oportunidades de intercâmbio durante a graduação. Durante a palestra, os participantes terão a oportunidade de aprender sobre os diferentes tipos de intercâmbio, os benefícios de participar de um programa de intercâmbio e as melhores práticas para escolher um destino de intercâmbio adequado.",
                activity_type=ACTIVITY_TYPE.INTERNSHIP_FAIR,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1679324400000, #Mon Mar 20 2023 15:00:00 GMT+0000
                end_date=1679331600000,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Carol Santarelli", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="Gabriel Santos", bio="Gabriel Santos é um ex-estudante da Universidade IMT que participou de um programa de intercâmbio para a França durante sua graduação. Durante sua estadia na França, Gabriel teve a oportunidade de trabalhar em uma empresa de tecnologia e, após retornar ao Brasil, fundou sua própria empresa de tecnologia. Ele é formado em Engenharia de Computação pela Universidade IMT e tem uma vasta experiência no setor de tecnologia.", company="Mauá"),
                          Speaker(name="Ana Silva", bio="João Costa é um ex-estudante da Universidade IMT que participou de um programa de intercâmbio para a Austrália durante sua graduação. Durante sua estadia na Austrália, João teve a oportunidade de trabalhar em uma startup de tecnologia e, após retornar ao Brasil, fundou sua própria startup. Ele é formado em Engenharia de Software pela Universidade IMT e tem uma vasta experiência no setor de startups e empreendedorismo.", company="Mauá")],
                total_slots=10,
                taken_slots=4,
                accepting_new_enrollments=False,
                stop_accepting_new_enrollments_before=None,
                confirmation_code='696969'
            ),

            Activity(
                code="ECM12321",
                title="Curso de Libras Básico",
                description="Este curso introdutório de Libras (Língua Brasileira de Sinais) tem como objetivo fornecer aos alunos uma compreensão básica da linguagem de sinais, incluindo a alfabetização em Libras, vocabulário básico, gramática e conversação. O curso também irá apresentar aos alunos a cultura surda e a importância da acessibilidade para pessoas surdas. O curso será ministrado por professores com ampla experiência no ensino de Libras.",
                activity_type=ACTIVITY_TYPE.COURSES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1679583600000, #Thu Mar 23 2023 15:00:00 GMT+0000
                end_date=1679587200000,
                link="www.maua.br",
                place="H321",
                responsible_professors=[
                    User(name="Carol Santarelli", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="Luís Carlos Santos", bio="Luís Carlos Santos é professor de Libras e intérprete com mais de 15 anos de experiência no ensino da língua de sinais e na interpretação para pessoas surdas em diversos contextos, incluindo escolas, empresas e eventos. Ele é formado em Letras/Libras pela Universidade Federal de São Paulo e já trabalhou em diversas organizações e instituições em todo o país. Além disso, Luís Carlos também é um defensor da inclusão e acessibilidade de pessoas surdas na sociedade.", company="LIBRAS Escola")],
                total_slots=100,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),

            Activity(
                code="PTPV12",
                title="Transfobia no Brasil: como combatê-la?",
                description="Palestra destinada a estudantes e profissionais da área de tecnologia e engenharia interessados em entender melhor a luta pela inclusão de pessoas trans e combate à transfobia. Durante a palestra, serão apresentados dados sobre a violência contra pessoas trans no Brasil, bem como as principais formas de discriminação que enfrentam no mercado de trabalho. Os palestrantes irão compartilhar suas experiências pessoais e discutir estratégias para promover a inclusão de pessoas trans em empresas e ambientes acadêmicos. A palestra tem como objetivo conscientizar e inspirar os participantes a agir de forma mais inclusiva e combater a transfobia em suas vidas pessoais e profissionais..",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1681743600000, #Mon Apr 17 2023 15:00:00 GMT+0000
                end_date=1681747200000,
                link=None,
                place="H321",
                responsible_professors=[
                    User(name="Maria Luiza", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Lucas Souza", bio="Lucas Souza é uma das lideranças do coletivo LGBTI+ da empresa XYZ e tem ampla experiência em projetos de inclusão e diversidade. Ele é formado em Administração pela Universidade Federal de São Paulo e tem mais de 8 anos de experiência em empresas de tecnologia. Lucas é um defensor dos direitos das pessoas trans e tem sido um importante aliado na luta contra a transfobia no ambiente corporativo.", company="Renner")],
                total_slots=5,
                taken_slots=5,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1681591435000, #Saturday, April 15, 2023 8:43:55 PM
                confirmation_code=None
            ),

        ]


def load_test():
    repo_activity = Environments.get_activity_repo()()
    stage = Environments.get_envs().stage
    dynamo_table_name = Environments.get_envs().dynamo_table_name
    print(stage, dynamo_table_name)
    activities = ActivityRepositoryMock().activities
    enrollments = ActivityRepositoryMock().enrollments

    print('Loading mock data to dynamo...')

    print('Loading activities with enrollments...')
    
    activity_example = activities[0]
    enrollment_example = enrollments[0]
    print(enrollment_example)

    start = time.time()
    for i in range(100):
        activity_example.code = f"ACT{i}"
        activity_example.title = f"Activity {i}"
        repo_activity.create_activity(activity_example)
        print(f'Loading activity {activity_example.code} | {activity_example.title}...')

        for j in range(50):
            enrollment_example.activity_code = f"ACT{i}"
            enrollment_example.user_id = f"USER{i}{j}"
            print(type(enrollment_example))
            repo_activity.create_enrollment(enrollment=enrollment_example)

        print(f'Loading enrollments {enrollment_example.activity_code} | {enrollment_example.user_id}...')
        
    end = time.time()
    
    print(f'100 activities with 50 enrollments each loaded in {end - start} seconds!\n')


if __name__ == '__main__':
    # load_test()


