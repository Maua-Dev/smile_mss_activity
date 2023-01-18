import datetime
from typing import List, Tuple

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
            User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="c695"),
            User(name="Rafael Santos", role=ROLE.PROFESSOR, user_id="12mf"),
            User(name="Rodrigo Santos", role=ROLE.PROFESSOR, user_id="b2f1"),
        ]

        self.activities = [
            Activity(
                code="ECM2345",
                title="Atividade da ECM 2345",
                description="Isso é uma atividade",
                activity_type=ACTIVITY_TYPE.COURSES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 19, 16, 52, 998305),
                duration=120,
                link=None,
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[self.speakers[0]],
                total_slots=4,
                taken_slots=4,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 18, 16, 52, 998305)
            ),
            Activity(
                code="ELET355",
                title="Atividade da ELET 355",
                description="Isso é uma atividade, sério.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=datetime.datetime(2022, 12, 21, 19, 16, 52, 998305),
                duration=400,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[self.users[10]],
                speakers=[self.speakers[1]],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="COD1468",
                title="Atividade da COD 1468",
                description="Isso definitivamente é uma atividade",
                activity_type=ACTIVITY_TYPE.HIGH_IMPACT_LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=datetime.datetime(2022, 12, 21, 19, 16, 52, 998305),
                duration=60,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[self.users[2], self.users[10]],
                speakers=[self.speakers[2]],
                total_slots=50,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="CODIGO",
                title="Atividade da CÓDIGO",
                description="Isso DEFINITIVAMENTE é uma atividade!",
                activity_type=ACTIVITY_TYPE.TECHNICAL_VISITS,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=datetime.datetime(2022, 12, 25, 19, 16, 52, 998305),
                duration=60,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[self.users[2]],
                speakers=[self.speakers[0], self.speakers[1], self.speakers[2]],
                total_slots=15,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 19, 16, 52, 998305)
            ),
            Activity(
                code="AC000",
                title="Atividade de competição",
                description="Isso é uma guerra",
                activity_type=ACTIVITY_TYPE.ACADEMIC_COMPETITIONS,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 21, 19, 16, 52, 998305),
                duration=190,
                link=None,
                place="H332",
                responsible_professors=[self.users[10]],
                speakers=[self.speakers[1]],
                total_slots=50,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 20, 19, 16, 52, 998305)
            ),
            Activity(
                code="ECM251",
                title="Atividade da ECM251",
                description="Se o professor chegar vai ter atividade...",
                activity_type=ACTIVITY_TYPE.HACKATHON,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=datetime.datetime(2022, 12, 22, 15, 16, 52, 998305),
                duration=40,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[self.users[10]],
                speakers=[self.speakers[2]],
                total_slots=20,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="SC456",
                title="Atividade da SC456",
                description="Sem criatividade para descrição",
                activity_type=ACTIVITY_TYPE.INTERNSHIP_FAIR,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.ONLINE,
                start_date=datetime.datetime(2022, 12, 20, 16, 16, 52, 998305),
                duration=80,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[self.users[2]],
                speakers=[self.speakers[0]],
                total_slots=10,
                taken_slots=1,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="CAFE",
                title="Atividade da CAFE",
                description="Atividade pra tomar café",
                activity_type=ACTIVITY_TYPE.ALUMNI_CAFE,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 21, 19, 16, 52, 998305),
                duration=20,
                link=None,
                place="H332",
                responsible_professors=[self.users[10]],
                speakers=[self.speakers[1]],
                total_slots=2,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="CODE",
                title="Atividade da CODE",
                description="O mesmo speaker pela 50° vez",
                activity_type=ACTIVITY_TYPE.PROFESSORS_ACADEMY,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305),
                duration=120,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[self.speakers[2]],
                total_slots=50,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="PRF246",
                title="Atividade da PRF246",
                description="Um único professor pra tudo",
                activity_type=ACTIVITY_TYPE.CULTURAL_ACTIVITY,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 25, 19, 16, 52, 998305),
                duration=140,
                link=None,
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[self.speakers[0]],
                total_slots=50,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="2468",
                title="Atividade da 2468",
                description="Atividade com números pares",
                activity_type=ACTIVITY_TYPE.GCSP,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=datetime.datetime(2022, 12, 25, 19, 16, 52, 998305),
                duration=60,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[self.speakers[1]],
                total_slots=25,
                taken_slots=0,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            ),
            Activity(
                code="ULTIMA",
                title="Última atividade",
                description="Atividade pra acabar",
                activity_type=ACTIVITY_TYPE.SPORTS_ACTIVITY,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 15, 16, 52, 998305),
                duration=45,
                link=None,
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[self.speakers[2]],
                total_slots=3,
                taken_slots=3,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 15, 16, 51, 998305)
            ),
            Activity(
                code="PINOQ1",
                title="Atividade da PINOQ1",
                description="Não era a última....",
                activity_type=ACTIVITY_TYPE.CULTURAL_ACTIVITY,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 2, 15, 16, 52, 998305),
                duration=45,
                link=None,
                place="H332",
                responsible_professors=[self.users[2]],
                speakers=[self.speakers[2], self.speakers[1]],
                total_slots=10,
                taken_slots=4,
                accepting_new_enrollments=False,
                stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 1, 15, 16, 51, 998305)
            ),

        ]

        self.enrollments = [
            Enrollment(activity=self.activities[0], user=self.users[0], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 16, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[0], user=self.users[1], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 17, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[0], user=self.users[2], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 18, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[0], user=self.users[3], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[0], user=self.users[4], state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=datetime.datetime(2022, 12, 20, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[0], user=self.users[5], state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=datetime.datetime(2022, 12, 20, 19, 17, 52, 998305)),
            Enrollment(activity=self.activities[0], user=self.users[6], state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=datetime.datetime(2022, 12, 20, 19, 18, 52, 998305)),
            Enrollment(activity=self.activities[1], user=self.users[1], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[2], user=self.users[3], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 51, 998305)),
            Enrollment(activity=self.activities[2], user=self.users[4], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[3], user=self.users[4], state=ENROLLMENT_STATE.REJECTED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[3], user=self.users[5], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 20, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[3], user=self.users[6], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 21, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[4], user=self.users[5], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 17, 16, 52, 998305)),
            Enrollment(activity=self.activities[4], user=self.users[6], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[5], user=self.users[6], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[6], user=self.users[7], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[7], user=self.users[8], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 18, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[7], user=self.users[1], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[7], user=self.users[2], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=datetime.datetime(2022, 12, 20, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[8], user=self.users[9], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=datetime.datetime(2022, 12, 17, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[9], user=self.users[0], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[10], user=self.users[1], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=datetime.datetime(2022, 12, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[11], user=self.users[1], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 10, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[11], user=self.users[2], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 11, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[11], user=self.users[3], state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=datetime.datetime(2022, 12, 12, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[11], user=self.users[5], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 12, 13, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[11], user=self.users[4], state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=datetime.datetime(2022, 12, 21, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[12], user=self.users[1], state=ENROLLMENT_STATE.COMPLETED,
                       date_subscribed=datetime.datetime(2022, 11, 19, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[12], user=self.users[2], state=ENROLLMENT_STATE.COMPLETED,
                       date_subscribed=datetime.datetime(2022, 11, 20, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[12], user=self.users[3], state=ENROLLMENT_STATE.COMPLETED,
                       date_subscribed=datetime.datetime(2022, 11, 21, 19, 16, 52, 998305)),
            Enrollment(activity=self.activities[12], user=self.users[4], state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=datetime.datetime(2022, 11, 29, 19, 16, 52, 998305)),
        ]

    def get_enrollment(self, user_id: str, code: str) -> Enrollment:
        for enrollment in self.enrollments:
            if enrollment.user.user_id == user_id and enrollment.activity.code == code:
                return enrollment
        return None

    def create_enrollment(self, enrollment : Enrollment) -> Enrollment:
        self.enrollments.append(enrollment)
        self.update_enrollment(enrollment.user.user_id, enrollment.activity.code, ENROLLMENT_STATE.ENROLLED)

        return enrollment
      
    def get_user(self, user_id : str) -> User:
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_activity(self, code:str) -> Activity:
        for activity in self.activities:
            if activity.code == code:
                return activity
        return None

    def update_enrollment(self, user_id: str, code: str, new_state: ENROLLMENT_STATE) -> Enrollment:
        for enrollment in self.enrollments:
            if enrollment.user.user_id == user_id and enrollment.activity.code == code:
                if new_state == ENROLLMENT_STATE.DROPPED:
                    self.update_activity(code=code, new_taken_slots=enrollment.activity.taken_slots - 1)
                elif new_state == ENROLLMENT_STATE.ENROLLED:
                    self.update_activity(code=code, new_taken_slots=enrollment.activity.taken_slots + 1)

                enrollment.state = new_state
                return enrollment
        return None

    def get_activity_with_enrollments(self, code: str) -> Tuple[Activity, List[Enrollment]]:
        for activity in self.activities:
            if activity.code == code:
                enrollments = [enrollment for enrollment in self.enrollments if enrollment.activity.code == code]
                return activity, enrollments
        return None, None

    def update_activity(self, code: str, new_title: str = None, new_description: str = None,
                        new_activity_type: ACTIVITY_TYPE = None, new_is_extensive: bool = None,
                        new_delivery_model: DELIVERY_MODEL = None, new_start_date: datetime.datetime = None,
                        new_duration: int = None, new_link: str = None, new_place: str = None,
                        new_responsible_professors: List[User] = None, new_speakers: List[Speaker] = None,
                        new_total_slots: int = None, new_taken_slots: int = None,
                        new_accepting_new_enrollments: bool = None,
                        new_stop_accepting_new_enrollments_before: datetime.datetime = None) -> Activity:
        for activity in self.activities:
            if activity.code == code:
                if new_title is not None:
                    activity.title = new_title
                if new_description is not None:
                    activity.description = new_description
                if new_activity_type is not None:
                    activity.activity_type = new_activity_type
                if new_is_extensive is not None:
                    activity.is_extensive = new_is_extensive
                if new_delivery_model is not None:
                    activity.delivery_model = new_delivery_model
                if new_start_date is not None:
                    activity.start_date = new_start_date
                if new_duration is not None:
                    activity.duration = new_duration
                if new_link is not None:
                    activity.link = new_link
                if new_place is not None:
                    activity.place = new_place
                if new_responsible_professors is not None:
                    activity.responsible_professors = new_responsible_professors
                if new_speakers is not None:
                    activity.speakers = new_speakers
                if new_total_slots is not None:
                    activity.total_slots = new_total_slots
                if new_taken_slots is not None:
                    activity.taken_slots = new_taken_slots
                if new_accepting_new_enrollments is not None:
                    activity.accepting_new_enrollments = new_accepting_new_enrollments
                if new_stop_accepting_new_enrollments_before is not None:
                    activity.stop_accepting_new_enrollments_before = new_stop_accepting_new_enrollments_before
                return activity

        return None

    def delete_activity(self, code: str) -> Activity:
        for idx, activity in enumerate(self.activities):
            if activity.code == code:
                 return self.activities.pop(idx)

        return None
