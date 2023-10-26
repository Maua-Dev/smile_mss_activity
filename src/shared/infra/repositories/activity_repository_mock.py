from typing import List, Tuple, Optional

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class ActivityRepositoryMock(IActivityRepository):
    speakers: List[Speaker]
    activities: List[Activity]
    enrollments: List[Enrollment]

    def __init__(self):
        users = UserRepositoryMock().users


        self.activities = [
            Activity(
                code="ECM2345",
                title="Atividade da ECM 2345",
                description="Isso é uma atividade",
                activity_type=ACTIVITY_TYPE.COURSES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671747413000,
                end_date=1671754613000,
                link=None,
                place="H332",
                responsible_professors=[User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                total_slots=4,
                taken_slots=4,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671743812000,
                confirmation_code=None
            ),
            Activity(
                code="ELET355",
                title="Atividade da ELET 355",
                description="Isso é uma atividade, sério.",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1671661013000,
                end_date=1695661013000,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=10,
                taken_slots=1,
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
                start_date=1671661013000,
                end_date=1671664613000,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002"), User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=50,
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
                start_date=1672006613000,
                end_date=1672010213000,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
                speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple"),
                          Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"),
                          Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=15,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671747413000,
                confirmation_code=None
            ),
            Activity(
                code="AC000",
                title="Atividade de competição",
                description="Isso é uma guerra",
                activity_type=ACTIVITY_TYPE.ACADEMIC_COMPETITIONS,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671661013000,
                end_date=1671672413000,
                link=None,
                place="H332",
                responsible_professors=[User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
                speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=50,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671574613000,
                confirmation_code=None
            ),
            Activity(
                code="ECM251",
                title="Atividade da ECM251",
                description="Se o professor chegar vai ter atividade...",
                activity_type=ACTIVITY_TYPE.HACKATHON,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.HYBRID,
                start_date=1671733013000,
                end_date=1671735413000,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
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
                start_date=1671563813000,
                end_date=1671568613000,
                link="https://devmaua.com",
                place=None,
                responsible_professors=[User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
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
                start_date=1671661013000,
                end_date=1671662213000,
                link=None,
                place="H332",
                responsible_professors=[User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
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
                start_date=1671488213000,
                end_date=1671495413000,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
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
                start_date=1672006613000,
                end_date=1672015013000,
                link=None,
                place="H332",
                responsible_professors=[User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
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
                start_date=1672006613000,
                end_date=1672010213000,
                link="https://devmaua.com",
                place="H332",
                responsible_professors=[User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
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
                start_date=1671733013000,
                end_date=1671735713000,
                link=None,
                place="H332",
                responsible_professors=[User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")],
                total_slots=3,
                taken_slots=3,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671733012000,
                confirmation_code="555666"
            ),
            Activity(
                code="PINOQ1",
                title="Atividade da PINOQ1",
                description="Não era a última....",
                activity_type=ACTIVITY_TYPE.CULTURAL_ACTIVITY,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1670005013000,
                end_date=1670007713000,
                link=None,
                place="H332",
                responsible_professors=[User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
                speakers=[Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung"),
                          Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
                total_slots=10,
                taken_slots=4,
                accepting_new_enrollments=False,
                stop_accepting_new_enrollments_before=1669918612000,
                confirmation_code='696969'
            ),

        ]
        self.enrollments = [
            Enrollment(activity_code=self.activities[0].code, user_id=users[0].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671229013000),
            Enrollment(activity_code=self.activities[0].code, user_id=users[1].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671315413000),
            Enrollment(activity_code=self.activities[0].code, user_id=users[2].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671401813000),
            Enrollment(activity_code=self.activities[0].code, user_id=users[3].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[0].code, user_id=users[4].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671574613000),
            Enrollment(activity_code=self.activities[0].code, user_id=users[5].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671574673000),
            Enrollment(activity_code=self.activities[0].code, user_id=users[6].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671574733000),
            Enrollment(activity_code=self.activities[1].code, user_id=users[1].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[2].code, user_id=users[3].user_id, state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671488212000),
            Enrollment(activity_code=self.activities[2].code, user_id=users[4].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[3].code, user_id=users[4].user_id, state=ENROLLMENT_STATE.REJECTED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[3].code, user_id=users[5].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671574613000),
            Enrollment(activity_code=self.activities[3].code, user_id=users[6].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671661013000),
            Enrollment(activity_code=self.activities[4].code, user_id=users[5].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671481013000),
            Enrollment(activity_code=self.activities[4].code, user_id=users[6].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[5].code, user_id=users[6].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[6].code, user_id=users[7].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[7].code, user_id=users[8].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671401813000),
            Enrollment(activity_code=self.activities[7].code, user_id=users[1].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[7].code, user_id=users[2].user_id, state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671574613000),
            Enrollment(activity_code=self.activities[8].code, user_id=users[9].user_id, state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671315413000),
            Enrollment(activity_code=self.activities[9].code, user_id=users[0].user_id, state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[10].code, user_id=users[1].user_id, state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1671488213000),
            Enrollment(activity_code=self.activities[11].code, user_id=users[1].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1670710613000),
            Enrollment(activity_code=self.activities[11].code, user_id=users[2].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1670710614000),
            Enrollment(activity_code=self.activities[11].code, user_id=users[3].user_id, state=ENROLLMENT_STATE.DROPPED,
                       date_subscribed=1670710615000),
            Enrollment(activity_code=self.activities[11].code, user_id=users[5].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1670710616000),
            Enrollment(activity_code=self.activities[11].code, user_id=users[4].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671661013000),
            Enrollment(activity_code=self.activities[12].code, user_id=users[1].user_id, state=ENROLLMENT_STATE.COMPLETED,
                       date_subscribed=1668896213000),
            Enrollment(activity_code=self.activities[12].code, user_id=users[2].user_id, state=ENROLLMENT_STATE.COMPLETED,
                       date_subscribed=1668982612000),
            Enrollment(activity_code=self.activities[12].code, user_id=users[3].user_id, state=ENROLLMENT_STATE.COMPLETED,
                       date_subscribed=1669069013000),
            Enrollment(activity_code=self.activities[12].code, user_id=users[4].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1669760213000),
        ]

    def get_enrollment(self, user_id: str, code: str) -> Enrollment:
        for enrollment in self.enrollments:
            if enrollment.user_id == user_id and enrollment.activity_code == code and enrollment.state != ENROLLMENT_STATE.DROPPED and enrollment.state != ENROLLMENT_STATE.ACTIVITY_CANCELLED:
                return enrollment
        return None

    def create_enrollment(self, enrollment: Enrollment) -> Enrollment:
        self.enrollments.append(enrollment)
        activity = self.get_activity(code=enrollment.activity_code)
        if enrollment.state == ENROLLMENT_STATE.ENROLLED:
            self.update_activity(code=enrollment.activity_code, new_taken_slots=activity.taken_slots + 1)

        return enrollment

    def get_activity(self, code: str) -> Activity:
        for activity in self.activities:
            if activity.code == code:
                return activity
        return None

    def update_enrollment(self, user_id: str, code: str, new_state: ENROLLMENT_STATE) -> Enrollment:
        old_enrollment = self.get_enrollment(user_id=user_id, code=code)

        for enrollment in self.enrollments:
            if enrollment.user_id == user_id and enrollment.activity_code == code:
                activity = self.get_activity(code=code)
                if new_state == ENROLLMENT_STATE.DROPPED:
                    self.update_activity(code=code, new_taken_slots=activity.taken_slots - 1)
                elif new_state == ENROLLMENT_STATE.ENROLLED:
                    if old_enrollment.state == ENROLLMENT_STATE.IN_QUEUE:
                        self.update_activity(code=code, new_taken_slots=activity.taken_slots + 1)
                    else:
                        self.update_activity(code=code, new_taken_slots=activity.taken_slots)

                enrollment.state = new_state
                return enrollment
        return None

    def get_activity_with_enrollments(self, code: str) -> Tuple[Activity, List[Enrollment]]:
        for activity in self.activities:
            if activity.code == code:
                enrollments = [enrollment for enrollment in self.enrollments if enrollment.activity_code == code]
                enrollments.sort(key=lambda x: (x.state != ENROLLMENT_STATE.COMPLETED, x.date_subscribed))
                return activity, enrollments
        return None, None

    def update_activity(self, code: Optional[str], new_title: Optional[str] = None, new_description: Optional[str] = None,
                        new_activity_type: Optional[ACTIVITY_TYPE] = None, new_is_extensive: Optional[bool] = None,
                        new_delivery_model: Optional[DELIVERY_MODEL] = None, new_start_date: Optional[int] = None,
                        new_end_date: Optional[int] = None, new_link: Optional[str] = None, new_place: Optional[str] = None,
                        new_responsible_professors: Optional[List[User]] = None, new_speakers: Optional[List[Speaker]] = None,
                        new_total_slots: Optional[int] = None, new_taken_slots: Optional[int] = None,
                        new_accepting_new_enrollments: Optional[bool] = None,
                        new_stop_accepting_new_enrollments_before: Optional[int] = None,
                        new_confirmation_code: Optional[str] = None) -> Activity:
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
                if new_end_date is not None:
                    activity.end_date = new_end_date
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

                activity.confirmation_code = new_confirmation_code

                return activity

        return None

    def get_all_activities_admin(self) -> List[Tuple[Activity, List[Enrollment]]]:
        activities_with_enrollments = list()
        for activity in self.activities:
            activity, enrollments = self.get_activity_with_enrollments(code=activity.code)
            activities_with_enrollments.append((activity, enrollments))
        return activities_with_enrollments

    def get_all_activities(self) -> List[Activity]:
        activities = list()
        for activity in self.activities:
            activities.append(activity)
        return activities

    def delete_activity(self, code: str) -> Activity:
        for idx, activity in enumerate(self.activities):
            if activity.code == code:
                return self.activities.pop(idx)
        return None

    def batch_update_enrollment(self, enrollments: List[Enrollment], state: ENROLLMENT_STATE) -> List[Enrollment]:
        new_enrollments = []
        for enrollment in enrollments:
            new_enrollment = self.update_enrollment(user_id=enrollment.user_id, code=enrollment.activity_code,
                                                    new_state=state)
            new_enrollments.append(new_enrollment)

        return new_enrollments

    def create_activity(self, activity: Activity) -> Activity:
        self.activities.append(activity)

        return activity

    def get_enrollments_by_user_id(self, user_id: str) -> List[Enrollment]:
        enrollments = list()
        for enrollment in self.enrollments:
            if enrollment.user_id == user_id and (enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE):
                enrollments.append(enrollment)
        return enrollments

    def get_all_activities_logged(self, user_id: str) -> Tuple[List[Activity], List[Enrollment]]:
        activities = list()
        for activity in self.activities:
            activities.append(activity)

        user_enrollments = list()
        pos = 1
        for enrollment in self.enrollments:
            if enrollment.user_id == user_id and (enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE  or enrollment.state == ENROLLMENT_STATE.COMPLETED):
                if enrollment.state == ENROLLMENT_STATE.IN_QUEUE:
                    enrollment.position = pos
                    pos += 1
                user_enrollments.append(enrollment)

        return activities, user_enrollments

    def send_enrolled_email(self, user: UserInfo, activity: Activity):
        # send email in real
        return True

    def send_deleted_user_email(self, user: UserInfo) -> bool:
        # send email in real
        return True

    def delete_enrollment(self, user_id: str, code: str) -> Enrollment:
        for idx, enrollment in enumerate(self.enrollments):
            if enrollment.user_id == user_id and enrollment.activity_code == code:
                return self.enrollments.pop(idx)

    def delete_certificates(self, email: str) -> True:
        # delete certificates in real
        return True

    def get_enrollments_by_user_id_with_dropped(self, user_id: str) -> List[Enrollment]:
        enrollments = list()
        for enrollment in self.enrollments:
            if enrollment.user_id == user_id:
                enrollments.append(enrollment)
        return enrollments
    
    def batch_get_activities(self, codes: List[str]) -> List[Activity]:
        activities = list()
        for activity in self.activities:
            if activity.code in codes:
                activities.append(activity)
        return activities
    
    def batch_delete_enrollments(self, user_ids: List[str], code: str) -> List[Enrollment]:
        deleted_enrollments = []
        
        for enrollment in self.enrollments:
            if enrollment.user_id in user_ids and enrollment.activity_code == code:
                deleted_enrollments.append(enrollment)
            
        for enrollment in deleted_enrollments:
            self.enrollments.remove(enrollment)
            
        
        return deleted_enrollments

