
import datetime
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ActivityRepositoryMock:

    def test_get_enrollment(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        enrollment = repo.get_enrollment('d61dbf66-a10f-11ed-a8fc-0242ac120002', 'ECM2345')

        assert type(enrollment) == Enrollment

    def test_get_enrollment_not_exists(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        enrollment = repo.get_enrollment('d61dbf66-a10f-11ed-a8fc-0242ac120002', 'CODIGO_INEXISTENTE')
        assert enrollment is None

    def test_get_activity(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity = repo.get_activity("CAFE")

        assert type(activity) == Activity

    def test_get_activity_not_exists(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity = repo.get_activity("CODIGO_INEXISTENTE")
        assert activity is None

    def test_create_enrollment(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        enrollment = Enrollment(activity_code='ECM2345', user_id=repo_user.users[0].user_id, state=ENROLLMENT_STATE.ENROLLED,
                                date_subscribed=1671229013000)

        len_before = len(repo.enrollments)
        enrollment_created = repo.create_enrollment(enrollment=enrollment)
        len_after = len(repo.enrollments)

        assert type(enrollment_created) == Enrollment
        assert repo.enrollments[0].activity_code == 'ECM2345'
        assert repo.enrollments[0].user_id == repo_user.users[0].user_id
        assert repo.enrollments[0].state == ENROLLMENT_STATE.ENROLLED
        assert repo.enrollments[0].date_subscribed == 1671229013000
        assert len_before == len_after - 1

    def test_update_enrollment_drop(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        taken_slots_before = repo.activities[0].taken_slots
        enrollment = repo.update_enrollment(user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002", code="ECM2345", new_state=ENROLLMENT_STATE.DROPPED)

        assert repo.activities[0].taken_slots == taken_slots_before - 1
        assert type(enrollment) == Enrollment
        assert enrollment.state == ENROLLMENT_STATE.DROPPED

    def test_update_enrollment_enroll(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        taken_slots_before = repo.activities[0].taken_slots
        enrollment = repo.update_enrollment(user_id="03555872-a110-11ed-a8fc-0242ac120002", code="ECM2345", new_state=ENROLLMENT_STATE.ENROLLED)

        assert repo.activities[0].taken_slots == taken_slots_before + 1
        assert type(enrollment) == Enrollment
        assert enrollment.state == ENROLLMENT_STATE.ENROLLED

    def test_get_activity_with_enrollments(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity, enrollments = repo.get_activity_with_enrollments("2468")

        assert type(activity) == Activity
        assert type(enrollments) == list

        assert all(type(enrollment) == Enrollment for enrollment in enrollments)
        assert len(enrollments) == 1

    def test_update_activity_title(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity = repo.update_activity(code="2468", new_title="Novo título")

        assert type(activity) == Activity
        assert activity.title == "Novo título"

    def test_update_activity_not_found(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity = repo.update_activity(code="CODIGO_INEXISTENTE", new_title="Novo Título")

        assert activity is None

    def test_update_activity_taken_slots(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity = repo.update_activity(code="2468", new_taken_slots=10)

        assert type(activity) == Activity
        assert activity.taken_slots == 10

    def test_update_activity_new_type(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity = repo.update_activity(code='2468', new_activity_type=ACTIVITY_TYPE.GCSP)

        assert type(activity) == Activity
        assert activity.activity_type == ACTIVITY_TYPE.GCSP

    def test_update_activity_new_responsible_professors(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity = repo.update_activity(code='2468', new_responsible_professors=[repo_user.users[2]])

        assert type(activity) == Activity
        assert activity.responsible_professors == [repo_user.users[2]]

    def test_get_all_activities_admin(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity_with_enrollments = repo.get_all_activities_admin()

        assert len(activity_with_enrollments) == len(repo.activities)
        assert all(type(activity) == Activity for activity, enrollments in activity_with_enrollments)
        assert all(all(type(enrollment) == Enrollment for enrollment in enrollments) for activity, enrollments in activity_with_enrollments)

    def test_get_all_activities(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activities = repo.get_all_activities()

        assert len(activities) == len(repo.activities)
        assert all(type(activity) == Activity for activity in activities)

    def test_delete_activity(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        len_before = len(repo.activities)
        activity = repo.delete_activity(code="2468")
        len_after = len(repo.activities)

        assert type(activity) == Activity
        assert len_before == len_after + 1

    def test_delete_activity_not_found(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        activity = repo.delete_activity(code="CODIGO_INEXISTENTE")

        assert activity is None

    def test_batch_update_enrollment(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        new_enrollments = repo.batch_update_enrollment(repo.enrollments, state=ENROLLMENT_STATE.DROPPED)

        assert all(enrollment.state == ENROLLMENT_STATE.DROPPED for enrollment in new_enrollments)
        assert all(enrollment.state == ENROLLMENT_STATE.DROPPED for enrollment in repo.enrollments)


    def test_create_activity(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        len_before = len(repo.activities)
        activity = repo.create_activity(
            Activity(
                code="newCode",
                title="Atividade da CAFE",
                description="Atividade pra tomar café",
                activity_type=ACTIVITY_TYPE.ALUMNI_CAFE,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671743813000,
                end_date=1671745013000,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Rodrigo Santos", role=ROLE.PROFESSOR, user_id="71f06f24-a110-11ed-a8fc-0242ac120002")
                ],
                speakers=[
                    Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")
                ],
                total_slots=2,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None,
                confirmation_code="123456",
            )
        )
        assert type(activity) == Activity
        assert len(repo.activities) == len_before + 1

    def test_get_enrollments_by_user_id(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        enrollments = repo.get_enrollments_by_user_id(repo_user.users[4].user_id)
        assert type(enrollments) == list
        assert all(type(enrollment) == Enrollment for enrollment in enrollments)
        assert all(enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE for enrollment in enrollments)
        assert len(enrollments) == 4
        assert all(enrollment.user_id == repo_user.users[4].user_id for enrollment in enrollments)

    def test_get_enrollments_by_user_id_more_enrollments(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        enrollments = repo.get_enrollments_by_user_id(repo_user.users[1].user_id)
        assert type(enrollments) == list
        assert all(type(enrollment) == Enrollment for enrollment in enrollments)
        assert all(enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE for enrollment in enrollments)
        assert len(enrollments) == 4

    def test_get_enrollments_by_user_id_no_enrollments(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        enrollments = repo.get_enrollments_by_user_id(repo_user.users[11].user_id)
        assert type(enrollments) == list
        assert all(type(enrollment) == Enrollment for enrollment in enrollments)
        assert len(enrollments) == 0

    def test_get_all_activities_logged(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        requester_user = repo_user.users[2]
        activities, user_enrollments = repo.get_all_activities_logged(user_id=requester_user.user_id)
        assert type(activities) == list
        assert all(type(activity) == Activity for activity in activities)
        assert len(activities) == len(repo.activities)

        assert type(user_enrollments) == list
        assert all(type(enrollment) == Enrollment for enrollment in user_enrollments)
        assert all(enrollment.user_id == requester_user.user_id for enrollment in user_enrollments)
        assert all(enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE or enrollment.state == ENROLLMENT_STATE.COMPLETED for enrollment in user_enrollments)
        assert len(user_enrollments) == 3

    def test_get_all_activities_logged_no_enrollments(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        requester_user = repo_user.users[12]
        activities, user_enrollments = repo.get_all_activities_logged(user_id=requester_user.user_id)
        assert type(activities) == list
        assert all(type(activity) == Activity for activity in activities)
        assert len(activities) == len(repo.activities)

        assert type(user_enrollments) == list
        assert all(type(enrollment) == Enrollment for enrollment in user_enrollments)
        assert len(user_enrollments) == 0

    def test_delete_enrollment(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        len_before = len(repo.enrollments)

        requester_user = repo_user.users[4]

        deleted_enrollment = repo.delete_enrollment(user_id=requester_user.user_id, code='ECM2345')

        assert len(repo.enrollments) == len_before - 1
        assert  type(deleted_enrollment) == Enrollment


    def test_delete_enrollment_not_found(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        len_before = len(repo.enrollments)

        requester_user = repo_user.users[4]

        deleted_enrollment = repo.delete_enrollment(user_id=requester_user.user_id, code='CODIGO_INEXISTENTE')

        assert len(repo.enrollments) == len_before
        assert deleted_enrollment is None

    def test_delete_certificates(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        requester_user = repo_user.users[-1]

        deleted_certificates = repo.delete_certificates(email=requester_user.email)

        assert deleted_certificates is True

    def test_send_deleted_user_email(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        requester_user = repo_user.users[-1]

        deleted_certificates = repo.send_deleted_user_email(user = requester_user)

        assert deleted_certificates is True
    
    def test_batch_get_activities(self):
        repo = ActivityRepositoryMock()

        activities = repo.batch_get_activities(['ECM2345', 'ELET355'])

        assert type(activities) == list
        assert all(type(activity) == Activity for activity in activities)
        
        assert activities[0] == Activity(
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
            )
        assert activities[1] == Activity(
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
            )
        
    def test_batch_delete_enrollments(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        requester_user = repo_user.users[-1]

        activity, enrollments = repo.get_activity_with_enrollments('CODIGO')

        deleted_enrollments = repo.batch_delete_enrollments([enrollment.user_id for enrollment in enrollments], activity.code)

        assert deleted_enrollments == enrollments  

    def test_get_activity_with_enrollments_sort(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        repo.enrollments.append(Enrollment(activity_code='ECM2345', user_id=repo_user.users[7].user_id, state=ENROLLMENT_STATE.COMPLETED,    
                                date_subscribed=1671229013000))
        repo.enrollments.append(Enrollment(activity_code='ECM2345', user_id=repo_user.users[8].user_id, state=ENROLLMENT_STATE.COMPLETED,
                                    date_subscribed=1669229013000)) 
        activity, enrollments = repo.get_activity_with_enrollments("ECM2345")



        assert type(activity) == Activity
        assert type(enrollments) == list

        assert all(type(enrollment) == Enrollment for enrollment in enrollments)
        assert len(enrollments) == 9
        
        assert enrollments[0] == Enrollment(activity_code='ECM2345', user_id=repo_user.users[8].user_id, state=ENROLLMENT_STATE.COMPLETED,
                                    date_subscribed=1669229013000)
        assert enrollments[1] == Enrollment(activity_code='ECM2345', user_id=repo_user.users[7].user_id, state=ENROLLMENT_STATE.COMPLETED,
                                    date_subscribed=1671229013000)
        assert enrollments[2] == Enrollment(activity_code='ECM2345', user_id=repo_user.users[0].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671229013000)
        assert enrollments[3] == Enrollment(activity_code='ECM2345', user_id=repo_user.users[1].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671315413000)
        assert enrollments[4] == Enrollment(activity_code='ECM2345', user_id=repo_user.users[2].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671401813000)
        assert enrollments[5] == Enrollment(activity_code='ECM2345', user_id=repo_user.users[3].user_id, state=ENROLLMENT_STATE.ENROLLED,
                       date_subscribed=1671488213000)
        assert enrollments[6] == Enrollment(activity_code='ECM2345', user_id=repo_user.users[4].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671574613000)
        assert enrollments[7] == Enrollment(activity_code='ECM2345', user_id=repo_user.users[5].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671574673000)
        assert enrollments[8] == Enrollment(activity_code='ECM2345', user_id=repo_user.users[6].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                       date_subscribed=1671574733000)
        
    def test_get_all_activities_logged_positions(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        requester_user = repo_user.users[2]

        repo.enrollments.append(Enrollment(activity_code='ECM2345', user_id=repo_user.users[2].user_id, state=ENROLLMENT_STATE.IN_QUEUE,    
                                    date_subscribed=1671229013000))
        repo.enrollments.append(Enrollment(activity_code='ECM2345', user_id=repo_user.users[2].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                                    date_subscribed=1669229013000)) 
        
        activities, user_enrollments = repo.get_all_activities_logged(user_id=requester_user.user_id)
        assert type(activities) == list
        assert all(type(activity) == Activity for activity in activities)
        assert len(activities) == len(repo.activities)

        assert type(user_enrollments) == list
        assert all(type(enrollment) == Enrollment for enrollment in user_enrollments)
        assert all(enrollment.user_id == requester_user.user_id for enrollment in user_enrollments)
        assert all(enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE or enrollment.state == ENROLLMENT_STATE.COMPLETED for enrollment in user_enrollments)
        assert len(user_enrollments) == 5

        assert user_enrollments[len(user_enrollments) - 2].position == 1
        assert user_enrollments[len(user_enrollments) - 1].position == 2


