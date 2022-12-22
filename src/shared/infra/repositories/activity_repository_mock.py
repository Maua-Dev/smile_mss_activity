import datetime
from typing import List

from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository


class ActivityRepositoryMock(IActivityRepository):
    speakers: List[Speaker]
    users: List[User]
    activities: List[Activity]
    enrollments: List[Enrollment]


    def __init__(self):
        self.speakers = [
            Speaker(name="Vitor Briquez", bio="Incrível", company="Apple"),
            Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"),
            Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")
        ]
        self.users = [
            User(name="João Vilas", role=ROLE.ADMIN, user_id="db43"),
            User(name="Bruno Soller", role=ROLE.STUDENT, user_id="b16f"),
            User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="d7f1"),
            User(name="Pedro Marcelino", role=ROLE.INTERNATIONAL_STUDENT, user_id="80fb"),
            User(name="Hector Guerrini", role=ROLE.EXTERNAL, user_id="9257"),
            User(name="Ricardo Soller", role=ROLE.EMPLOYEE, user_id="f664"),
            User(name="Marcos Romanato", role=ROLE.STUDENT, user_id="bea2"),
            User(name="Marco Briquez", role=ROLE.STUDENT, user_id="f26f"),
            User(name="Simone Romanato", role=ROLE.EXTERNAL, user_id="d23a"),
            User(name="Viviani Soller", role=ROLE.EXTERNAL, user_id="d673"),
        ]
        self.enrollments = [
            Enrollment(activity=self.activities[0], user=self.users[0], state=ENROLLMENT_STATE.WAITING_LIST, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[1], user=self.users[1], state=ENROLLMENT_STATE.COMPLETED, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[2], user=self.users[3], state=ENROLLMENT_STATE.DROPPED, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[3], user=self.users[4], state=ENROLLMENT_STATE.REJECTED, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[4], user=self.users[5], state=ENROLLMENT_STATE.ENROLLED, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[5], user=self.users[6], state=ENROLLMENT_STATE.WAITING_LIST, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[6], user=self.users[7], state=ENROLLMENT_STATE.COMPLETED, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[7], user=self.users[8], state=ENROLLMENT_STATE.ENROLLED, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[8], user=self.users[9], state=ENROLLMENT_STATE.REJECTED, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[9], user=self.users[0], state=ENROLLMENT_STATE.REJECTED, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[10], user=self.users[1], state=ENROLLMENT_STATE.DROPPED, date_subscribed=datetime.datetime.today),
            Enrollment(activity=self.activities[11], user=self.users[3], state=ENROLLMENT_STATE.WAITING_LIST, date_subscribed=datetime.datetime.today)
        ]
        self.activities = [
            Activity(
                code="ECM2345",
                title="Atividade da ECM 2345",
                description="Isso é uma atividade",
                activity_type=ACTIVITY_TYPE.COURSES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.date.today,
                duration=120,
                encharged_professors=self.users[2],
                speakers=self.speakers[0],
                enrollments=self.enrollments[0],
                total_slots=20,
                taken_slots=10,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.date.today+5
            ),
            Activity(
                code="ELET355",
                title="Atividade da ELET 355",
                description="Isso é uma atividade, sério.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=datetime.date.today,
                duration=400,
                encharged_professors=self.users[2],
                speakers=self.speakers[1],
                enrollments=self.enrollments[1],
                total_slots=10,
                taken_slots=10,
                accepting_new_subscriptions=False,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="COD1468",
                title="Atividade da COD 1468",
                description="Isso definitivamente é uma atividade",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=datetime.date.today,
                duration=60,
                encharged_professors=self.users[2],
                speakers=self.speakers[2],
                enrollments=self.enrollments[2],
                total_slots=50,
                taken_slots=10,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="CÓDIGO",
                title="Atividade da CÓDIGO",
                description="Isso DEFINITIVAMENTE é uma atividade!",
                activity_type=ACTIVITY_TYPE.TECHNICAL_VISITS,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=datetime.date.today,
                duration=60,
                encharged_professors=self.users[2],
                speakers=self.speakers[0],
                enrollments=self.enrollments[3],
                total_slots=15,
                taken_slots=10,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="AC000",
                title="Atividade de competição",
                description="Isso é uma guerra",
                activity_type=ACTIVITY_TYPE.ACADEMIC_COMPETITIONS,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.date.today,
                duration=190,
                encharged_professors=self.users[2],
                speakers=self.speakers[1],
                enrollments=self.enrollments[4],
                total_slots=50,
                taken_slots=10,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="ECM251",
                title="Atividade da ECM251",
                description="Se o professor chegar vai ter atividade...",
                activity_type=ACTIVITY_TYPE.HACKATHON,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=datetime.date.today,
                duration=40,
                encharged_professors=self.users[2],
                speakers=self.speakers[2],
                enrollments=self.enrollments[5],
                total_slots=20,
                taken_slots=10,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="SC456",
                title="Atividade da SC456",
                description="Sem criatividade para descrição",
                activity_type=ACTIVITY_TYPE.INTERNSHIP_FAIR,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=datetime.date.today,
                duration=80,
                encharged_professors=self.users[2],
                speakers=self.speakers[0],
                enrollments=self.enrollments[6],
                total_slots=10,
                taken_slots=10,
                accepting_new_subscriptions=False,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="CAFE",
                title="Atividade da CAFE",
                description="Atividade pra tomar café",
                activity_type=ACTIVITY_TYPE.ALUMNI_CAFE,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.date.today,
                duration=20,
                encharged_professors=self.users[2],
                speakers=self.speakers[1],
                enrollments=self.enrollments[7],
                total_slots=10,
                taken_slots=10,
                accepting_new_subscriptions=False,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="CODE",
                title="Atividade da CODE",
                description="O mesmo speaker pela 50° vez",
                activity_type=ACTIVITY_TYPE.PROFESSORS_ACADEMY,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=datetime.date.today,
                duration=120,
                encharged_professors=self.users[2],
                speakers=self.speakers[2],
                enrollments=self.enrollments[8],
                total_slots=50,
                taken_slots=10,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="PRF246",
                title="Atividade da PRF246",
                description="Um único professor pra tudo",
                activity_type=ACTIVITY_TYPE.CULTURAL_ACTIVITY,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.date.today,
                duration=140,
                encharged_professors=self.users[2],
                speakers=self.speakers[0],
                enrollments=self.enrollments[9],
                total_slots=50,
                taken_slots=10,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="2468",
                title="Atividade da 2468",
                description="Atividade com números pares",
                activity_type=ACTIVITY_TYPE.GCSP,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=datetime.date.today,
                duration=60,
                encharged_professors=self.users[2],
                speakers=self.speakers[1],
                enrollments=self.enrollments[10],
                total_slots=25,
                taken_slots=10,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.date.today
            ),
            Activity(
                code="ULTIMA",
                title="Última atividade",
                description="Atividade pra acabar",
                activity_type=ACTIVITY_TYPE.SPORTS_ACTIVITY,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.date.today,
                duration=45,
                encharged_professors=self.users[2],
                speakers=self.speakers[2],
                enrollments=self.enrollments[11],
                total_slots=5,
                taken_slots=10,
                accepting_new_subscriptions=False,
                stop_accepting_new_subscriptions_before=datetime.date.today
            )
        ]
        