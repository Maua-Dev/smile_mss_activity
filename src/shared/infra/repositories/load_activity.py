from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.environments import Environments


class LoadActivityRepositoryMock:
    activities = List[Activity]

    def __init__(self) -> None:
        self.activities = [
            Activity(
                code="ECM2345",
                title="Inovação e Tecnologia para o Futuro",
                description="Isso é uma atividade",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1677348000000, #Sat Feb 25 2023 15:00
                duration=120,
                link=None,
                place="H332",
                responsible_professors=[User(name="Carol Mota", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[
                    Speaker(name="João Silva", bio="João Silva é o fundador e CEO da Tech Innovate, uma empresa de tecnologia que cria soluções inovadoras para problemas complexos. Ele tem mais de 20 anos de experiência em liderança empresarial e tecnologia. João já foi palestrante em diversas conferências e é reconhecido como uma das principais autoridades em inovação no Brasil.", company="Tech Innovate")
                ],
                total_slots=4,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1677337200000, #Sat Feb 25 2023 12:00
                confirmation_code=None
            ),
            Activity(
                code="ELET355",
                title="Atividade da ELET 355",
                description="Isso é uma atividade, sério.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1677250800000, #Fri Feb 24 2023 12:00
                duration=400,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name="Maria Vernasqui", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
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
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1672327600, #Tue Mar 01 2023 15:00
                duration=240,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Maria Vernasqui", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Rafaela Oliveira ", bio="Rafaela Oliveira é engenheira de materiais e atua na área de pesquisa e desenvolvimento da empresa DEF, fornecedora de peças para a indústria automotiva. Ela possui experiência na fabricação de materiais avançados utilizados em carros elétricos, como ligas de alumínio e polímeros de alta resistência.", company="Samsung")],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="CODIGO",
                title="Hackathon de Desenvolvimento de Software",
                description="O Hackathon de Desenvolvimento de Software é um evento que reunirá estudantes de engenharia e tecnologia para competir em equipes na criação de soluções de software inovadoras. Os participantes terão a oportunidade de trabalhar em projetos desafiadores, aprender novas habilidades e se conectar com profissionais do setor.",
                activity_type=ACTIVITY_TYPE.HACKATHON,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1661577600, #Wed Mar 02 2023 16:00
                duration=540,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Carol Mota", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="Ana Silva", bio="Ana Silva é diretora de tecnologia na empresa ABC, onde lidera a equipe de desenvolvimento de software. Ela possui mais de 15 anos de experiência em tecnologia, tendo trabalhado em empresas como Microsoft e Google.", company="Apple"),
                          Speaker(name="Pedro Oliveira", bio="Professor de engenharia de software na universidade XYZ. Ele é um especialista em metodologias ágeis de desenvolvimento de software e tem sido um mentor de sucesso em hackathons anteriores.", company="Microsoft"),
                          Speaker(name="Maria Santos ", bio="Gerente de produto na empresa DEF, onde lidera a equipe de desenvolvimento de novos produtos. Ela é uma especialista em UX/UI design e tem trabalhado em projetos inovadores na área de tecnologia.", company="Samsung")],
                total_slots=15,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1661577600,
                confirmation_code=None
            ),
            Activity(
                code="AC000",
                title="Tendências em tecnologia e engenharia",
                description="Esta palestra apresentará as tendências mais recentes em tecnologia e engenharia, abordando desde a evolução das linguagens de programação até as novidades em inteligência artificial e robótica. Será uma excelente oportunidade para atualizar-se sobre as mais recentes inovações em áreas tão importantes para a economia mundial.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1664908800, #Fri Mar 05 2023 12:00
                duration=120,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Maria Vernasqui", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
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
                start_date=1672474800,#
                duration=120,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name="Maria Vernasqui", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Marcos Oliveira", bio=" é diretor de tecnologia na empresa DEF, onde lidera a equipe responsável pelo desenvolvimento de soluções de internet das coisas para a indústria. Ele possui mais de 20 anos de experiência em tecnologia e engenharia, tendo trabalhado em empresas como Intel e Cisco.", company="DEF")],
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
                start_date=1678449600000, #Thu Mar 10 2023 09:10
                duration=80,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Carol Mota", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="CAFE",
                title="Tecnologias disruptivas e o futuro da engenharia",
                description="Nesta palestra, serão apresentadas as principais tendências e tecnologias disruptivas que estão moldando o futuro da engenharia. Serão discutidos tópicos como inteligência artificial, internet das coisas, realidade virtual e aumentada, além das possibilidades de aplicação dessas tecnologias em diferentes setores da indústria.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1646175600,
                duration=180,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Maria Vernasqui", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Ana Santos", bio="Ana Santos é especialista em inteligência artificial e inovação na indústria de engenharia. Ela trabalha na empresa DEF, onde lidera a equipe de pesquisa e desenvolvimento em inteligência artificial. Possui mais de 10 anos de experiência em pesquisa e desenvolvimento em inteligência artificial, tendo trabalhado em projetos inovadores em empresas como IBM e Microsoft.", company="DEF")],
                total_slots=2,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="CODE",
                title="Atividade da CODE",
                description="O Hackathon de Tecnologia e Engenharia é um evento em que equipes multidisciplinares terão a oportunidade de criar soluções inovadoras para desafios reais da indústria de tecnologia e engenharia. O objetivo é fomentar a criatividade, o trabalho em equipe e o desenvolvimento de habilidades técnicas e de negócios.",
                activity_type=ACTIVITY_TYPE.HACKATHON,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1646247600,
                duration=660,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name= "Carol Mota", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
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
                start_date=1677852000000, #Tue Mar 03 2023 11:00
                duration=140,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Carol Mota", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
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
                start_date=1646896800,
                duration=360,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name="Carol Mota", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="José Silva", bio="João é gerente de recursos humanos da empresa TechPlay, onde lidera a equipe responsável pelo recrutamento, seleção e desenvolvimento de talentos. Além disso, Pedro é um ávido jogador de futebol e está ansioso para organizar este campeonato interdepartamental.", company="TechPlay")],
                total_slots=25,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="ULTIMA",
                title="Encontro de Ex-Alunos: Tecnologia e Carreira",
                description=" O Encontro de Ex-Alunos: Tecnologia e Carreira é um evento organizado pela empresa TechPlay, com o objetivo de reunir ex-alunos da instituição para discutir temas relacionados à tecnologia e ao mercado de trabalho. Durante o evento, os participantes terão a oportunidade de compartilhar suas experiências e aprendizados, trocar ideias e fazer networking.",
                activity_type=ACTIVITY_TYPE.ALUMNI_CAFE,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1677675600000, #Mon Mar 01 2023 10:00
                duration=45,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Carol Mota", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="João Silva", bio=" ex-aluno da TechPlay e atualmente é líder técnico em uma startup de tecnologia. Ele irá compartilhar sua experiência em trabalhar em empresas de diferentes tamanhos e setores, falar sobre os desafios e oportunidades de trabalhar em uma startup e responder às perguntas dos participantes.", company="TechPlay")],
                total_slots=3,
                taken_slots=3,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1677646800000,
                confirmation_code="555666"
            ),
            Activity(
                code="PINOQ1",
                title="Palestra sobre Intercâmbio na Faculdade",
                description="A Palestra sobre Intercâmbio na Faculdade é um evento que tem como objetivo informar os estudantes universitários sobre as oportunidades de intercâmbio durante a graduação. Durante a palestra, os participantes terão a oportunidade de aprender sobre os diferentes tipos de intercâmbio, os benefícios de participar de um programa de intercâmbio e as melhores práticas para escolher um destino de intercâmbio adequado.",
                activity_type=ACTIVITY_TYPE.INTERNSHIP_FAIR,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1678215600000, #Sat Mar 07 2023 16:00
                duration=120,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Carol Mota", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="Gabriel Santos", bio="Gabriel Santos é um ex-estudante da Universidade IMT que participou de um programa de intercâmbio para a França durante sua graduação. Durante sua estadia na França, Gabriel teve a oportunidade de trabalhar em uma empresa de tecnologia e, após retornar ao Brasil, fundou sua própria empresa de tecnologia. Ele é formado em Engenharia de Computação pela Universidade IMT e tem uma vasta experiência no setor de tecnologia.", company="Mauá"),
                          Speaker(name="Ana Silva", bio="João Costa é um ex-estudante da Universidade IMT que participou de um programa de intercâmbio para a Austrália durante sua graduação. Durante sua estadia na Austrália, João teve a oportunidade de trabalhar em uma startup de tecnologia e, após retornar ao Brasil, fundou sua própria startup. Ele é formado em Engenharia de Software pela Universidade IMT e tem uma vasta experiência no setor de startups e empreendedorismo.", company="Mauá")],
                total_slots=10,
                taken_slots=4,
                accepting_new_enrollments=False,
                stop_accepting_new_enrollments_before=None,
                confirmation_code='696969'
            ),

            Activity(
                code="CODIGODOIS",
                title="Curso de Libras Básico",
                description="Este curso introdutório de Libras (Língua Brasileira de Sinais) tem como objetivo fornecer aos alunos uma compreensão básica da linguagem de sinais, incluindo a alfabetização em Libras, vocabulário básico, gramática e conversação. O curso também irá apresentar aos alunos a cultura surda e a importância da acessibilidade para pessoas surdas. O curso será ministrado por professores com ampla experiência no ensino de Libras.",
                activity_type=ACTIVITY_TYPE.COURSES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1678226400000, #Fri Mar 07 2023 19:00
                duration=60,
                link="www.maua.br",
                place="H321",
                responsible_professors=[
                    User(name="Carol Mota", role=ROLE.PROFESSOR, user_id="995eb33a-88f6-4c47-8ed1-7834302d0579")],
                speakers=[Speaker(name="Luís Carlos Santos", bio="Luís Carlos Santos é professor de Libras e intérprete com mais de 15 anos de experiência no ensino da língua de sinais e na interpretação para pessoas surdas em diversos contextos, incluindo escolas, empresas e eventos. Ele é formado em Letras/Libras pela Universidade Federal de São Paulo e já trabalhou em diversas organizações e instituições em todo o país. Além disso, Luís Carlos também é um defensor da inclusão e acessibilidade de pessoas surdas na sociedade.", company="LIBRAS Escola")],
                total_slots=100,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),

            Activity(
                code="UMDOISTRES",
                title="Transfobia no Brasil: como combatê-la?",
                description="Palestra destinada a estudantes e profissionais da área de tecnologia e engenharia interessados em entender melhor a luta pela inclusão de pessoas trans e combate à transfobia. Durante a palestra, serão apresentados dados sobre a violência contra pessoas trans no Brasil, bem como as principais formas de discriminação que enfrentam no mercado de trabalho. Os palestrantes irão compartilhar suas experiências pessoais e discutir estratégias para promover a inclusão de pessoas trans em empresas e ambientes acadêmicos. A palestra tem como objetivo conscientizar e inspirar os participantes a agir de forma mais inclusiva e combater a transfobia em suas vidas pessoais e profissionais..",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1678561200000, #Tue Mar 11 2023 16:00
                duration=60,
                link=None,
                place="H321",
                responsible_professors=[
                    User(name="Maria Vernasqui", role=ROLE.PROFESSOR, user_id="e5c26176-6a53-4e48-a085-fc92ea1b1c7f")],
                speakers=[Speaker(name="Lucas Souza", bio="Lucas Souza é uma das lideranças do coletivo LGBTI+ da empresa XYZ e tem ampla experiência em projetos de inclusão e diversidade. Ele é formado em Administração pela Universidade Federal de São Paulo e tem mais de 8 anos de experiência em empresas de tecnologia. Lucas é um defensor dos direitos das pessoas trans e tem sido um importante aliado na luta contra a transfobia no ambiente corporativo.", company="Renner")],
                total_slots=5,
                taken_slots=5,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1656796800,
                confirmation_code=None
            ),

        ]


if __name__ == '__main__':

    repo_activity = Environments.get_activity_repo()()
    activities = LoadActivityRepositoryMock().activities

    for activity in activities:
        try:
            new_activity = repo_activity.create_activity(activity)

            print(new_activity)

        except Exception as e:
            print("Erro ao criar atividade: ", e)
