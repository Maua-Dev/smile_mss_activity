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
                title="Atividade da ECM 2345",
                description="Isso é uma atividade",
                activity_type=ACTIVITY_TYPE.COURSES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1677348000000, #Sat Feb 25 2023 15:00
                duration=120,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Gep Soller", role=ROLE.PROFESSOR, user_id="31bc6c25-af3b-4fbc-bc38-cc5ef72256b7")],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
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
                    User(name="Vitor Guirão", role=ROLE.PROFESSOR, user_id="1d092927-2015-4963-b83d-c9ba46547dd2")],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=10,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="COD1468",
                title="Atividade da COD 1468",
                description="Isso definitivamente é uma atividade",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1677693600000, #Tue Mar 01 2023 15:00
                duration=60,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Vitor Guirão", role=ROLE.PROFESSOR, user_id="1d092927-2015-4963-b83d-c9ba46547dd2")],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="CODIGO",
                title="Atividade da CÓDIGO",
                description="Isso DEFINITIVAMENTE é uma atividade!",
                activity_type=ACTIVITY_TYPE.TECHNICAL_VISITS,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1677783600000, #Wed Mar 02 2023 16:00
                duration=60,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Gep Soller", role=ROLE.PROFESSOR, user_id="31bc6c25-af3b-4fbc-bc38-cc5ef72256b7")],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple"),
                          Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"),
                          Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=15,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1677758400000,
                confirmation_code=None
            ),
            Activity(
                code="AC000",
                title="Atividade de competição",
                description="Isso é uma guerra",
                activity_type=ACTIVITY_TYPE.ACADEMIC_COMPETITIONS,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1678032000000, #Fri Mar 05 2023 12:00
                duration=190,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Vitor Guirão", role=ROLE.PROFESSOR, user_id="1d092927-2015-4963-b83d-c9ba46547dd2")],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=15,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="ECM251",
                title="Atividade da ECM251",
                description="Se o professor chegar vai ter atividade...",
                activity_type=ACTIVITY_TYPE.HACKATHON,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1678302000000, #Tue Mar 08 2023 16:00
                duration=40,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name="Vitor Guirão", role=ROLE.PROFESSOR, user_id="1d092927-2015-4963-b83d-c9ba46547dd2")],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=20,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="SC456",
                title="Atividade da SC456",
                description="Sem criatividade para descrição",
                activity_type=ACTIVITY_TYPE.INTERNSHIP_FAIR,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=1678449600000, #Thu Mar 10 2023 09:10
                duration=80,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Gep Soller", role=ROLE.PROFESSOR, user_id="31bc6c25-af3b-4fbc-bc38-cc5ef72256b7")],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="CAFE",
                title="Atividade da CAFE",
                description="Atividade pra tomar café",
                activity_type=ACTIVITY_TYPE.ALUMNI_CAFE,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1678572000000, #Fri Mar 11 2023 19:00
                duration=20,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Vitor Guirão", role=ROLE.PROFESSOR, user_id="1d092927-2015-4963-b83d-c9ba46547dd2")],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=2,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="CODE",
                title="Atividade da CODE",
                description="O mesmo speaker pela 50° vez",
                activity_type=ACTIVITY_TYPE.PROFESSORS_ACADEMY,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1678878000000, #Tue Mar 15 2023 08:00
                duration=120,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name="Gep Soller", role=ROLE.PROFESSOR, user_id="31bc6c25-af3b-4fbc-bc38-cc5ef72256b7")],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=50,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="PRF246",
                title="Atividade da PRF246",
                description="Um único professor pra tudo",
                activity_type=ACTIVITY_TYPE.CULTURAL_ACTIVITY,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1677852000000, #Tue Mar 03 2023 11:00
                duration=140,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Gep Soller", role=ROLE.PROFESSOR, user_id="31bc6c25-af3b-4fbc-bc38-cc5ef72256b7")],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                total_slots=50,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="2468",
                title="Atividade da 2468",
                description="Atividade com números pares",
                activity_type=ACTIVITY_TYPE.GCSP,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1677970800000, #Wed Mar 04 2023 20:00
                duration=60,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[
                    User(name="Gep Soller", role=ROLE.PROFESSOR, user_id="31bc6c25-af3b-4fbc-bc38-cc5ef72256b7")],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=25,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),
            Activity(
                code="ULTIMA",
                title="Última atividade",
                description="Atividade pra acabar",
                activity_type=ACTIVITY_TYPE.SPORTS_ACTIVITY,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1677675600000, #Mon Mar 01 2023 10:00
                duration=45,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Gep Soller", role=ROLE.PROFESSOR, user_id="31bc6c25-af3b-4fbc-bc38-cc5ef72256b7")],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=3,
                taken_slots=3,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1677646800000,
                confirmation_code="555666"
            ),
            Activity(
                code="PINOQ1",
                title="Atividade da PINOQ1",
                description="Não era a última....",
                activity_type=ACTIVITY_TYPE.CULTURAL_ACTIVITY,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1678215600000, #Sat Mar 07 2023 16:00
                duration=45,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Gep Soller", role=ROLE.PROFESSOR, user_id="31bc6c25-af3b-4fbc-bc38-cc5ef72256b7")],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung"),
                          Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=10,
                taken_slots=4,
                accepting_new_enrollments=False,
                stop_accepting_new_enrollments_before=None,
                confirmation_code='696969'
            ),

            Activity(
                code="CODIGODOIS",
                title="Atividade com um CODIGODOIS",
                description="Isso é uma atividade com CODIGODOIS",
                activity_type=ACTIVITY_TYPE.ALUMNI_CAFE,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1678226400000, #Fri Mar 07 2023 19:00
                duration=60,
                link=None,
                place="H321",
                responsible_professors=[
                    User(name="Gep Soller", role=ROLE.PROFESSOR, user_id="31bc6c25-af3b-4fbc-bc38-cc5ef72256b7")],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                total_slots=100,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code=None
            ),

            Activity(
                code="UMDOISTRES",
                title="Atividade com números escritos",
                description="Isso definitivamente é uma atividade. Com números.",
                activity_type=ACTIVITY_TYPE.GCSP,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1678561200000, #Tue Mar 11 2023 16:00
                duration=60,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[
                    User(name="Vitor Guirão", role=ROLE.PROFESSOR, user_id="1d092927-2015-4963-b83d-c9ba46547dd2")],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=5,
                taken_slots=5,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1678557600000,
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
