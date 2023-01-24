
import datetime
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_ActivityRepositoryMock:

    def test_get_enrollment(self):
        repo = ActivityRepositoryMock()
        enrollment = repo.get_enrollment('db43', 'ECM2345')

        assert type(enrollment) == Enrollment

    def test_get_enrollment_not_exists(self):
        repo = ActivityRepositoryMock()
        enrollment = repo.get_enrollment('db43', 'CODIGO_INEXISTENTE')
        assert enrollment is None

    def test_get_activity(self):
        repo = ActivityRepositoryMock()
        activity = repo.get_activity("CAFE")

        assert type(activity) == Activity

    def test_get_activity_not_exists(self):
        repo = ActivityRepositoryMock()
        activity = repo.get_activity("CODIGO_INEXISTENTE")
        assert activity is None


    def test_get_user(self):
        repo = ActivityRepositoryMock()
        user = repo.get_user('db43')
        assert type(user) == User  

    def test_get_user_not_exists(self):
        repo = ActivityRepositoryMock()
        user = repo.get_user('NAO-EXISTE')
        assert user is None

    def test_create_enrollment(self):
        repo = ActivityRepositoryMock()
        enrollment = Enrollment(
            repo.get_activity('ECM2345'),
            repo.get_user('db43'),
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=1671229013000000
        )

        len_before = len(repo.enrollments)
        enrollment_created = repo.create_enrollment(enrollment=enrollment)
        len_after = len(repo.enrollments)

        assert type(enrollment_created) == Enrollment
        assert repo.enrollments[0].activity == repo.get_activity('ECM2345')
        assert repo.enrollments[0].user == repo.get_user('db43')
        assert repo.enrollments[0].state == ENROLLMENT_STATE.ENROLLED
        assert repo.enrollments[0].date_subscribed == 1671229013000000
        assert len_before == len_after - 1

    def test_update_enrollment_drop(self):
        repo = ActivityRepositoryMock()
        taken_slots_before = repo.activities[0].taken_slots
        enrollment = repo.update_enrollment(user_id="db43", code="ECM2345", new_state=ENROLLMENT_STATE.DROPPED)

        assert repo.activities[0].taken_slots == taken_slots_before - 1
        assert type(enrollment) == Enrollment
        assert enrollment.state == ENROLLMENT_STATE.DROPPED

    def test_update_enrollment_enroll(self):
        repo = ActivityRepositoryMock()
        taken_slots_before = repo.activities[0].taken_slots
        enrollment = repo.update_enrollment(user_id="9257", code="ECM2345", new_state=ENROLLMENT_STATE.ENROLLED)

        assert repo.activities[0].taken_slots == taken_slots_before + 1
        assert type(enrollment) == Enrollment
        assert enrollment.state == ENROLLMENT_STATE.ENROLLED

    def test_get_activity_with_enrollments(self):
        repo = ActivityRepositoryMock()
        activity, enrollments = repo.get_activity_with_enrollments("2468")

        assert type(activity) == Activity
        assert type(enrollments) == list

        assert all(type(enrollment) == Enrollment for enrollment in enrollments)
        assert len(enrollments) == 1

    def test_update_activity_title(self):
        repo = ActivityRepositoryMock()
        activity = repo.update_activity(code="2468", new_title="Novo título")

        assert type(activity) == Activity
        assert activity.title == "Novo título"

    def test_update_activity_not_found(self):
        repo = ActivityRepositoryMock()
        activity = repo.update_activity(code="CODIGO_INEXISTENTE", new_title="Novo Título")

        assert activity is None

    def test_update_activity_taken_slots(self):
        repo = ActivityRepositoryMock()
        activity = repo.update_activity(code="2468", new_taken_slots=10)

        assert type(activity) == Activity
        assert activity.taken_slots == 10

    def test_get_all_activities_admin(self):
        repo = ActivityRepositoryMock()
        activity_with_enrollments = repo.get_all_activities_admin()

        assert len(activity_with_enrollments) == len(repo.activities)
        assert all(type(activity) == Activity for activity, enrollments in activity_with_enrollments)
        assert all(all(type(enrollment) == Enrollment for enrollment in enrollments) for activity, enrollments in activity_with_enrollments)

    def test_get_all_activities(self):
        repo = ActivityRepositoryMock()
        activities = repo.get_all_activities()

        assert len(activities) == len(repo.activities)
        assert all(type(activity) == Activity for activity in activities)

    def test_delete_activity(self):
        repo = ActivityRepositoryMock()
        len_before = len(repo.activities)
        activity = repo.delete_activity(code="2468")
        len_after = len(repo.activities)

        assert type(activity) == Activity
        assert len_before == len_after + 1

    def test_delete_activity_not_found(self):
        repo = ActivityRepositoryMock()
        activity = repo.delete_activity(code="CODIGO_INEXISTENTE")

        assert activity is None

    def test_batch_update_enrollment(self):
        repo = ActivityRepositoryMock()
        new_enrollments = repo.batch_update_enrollment(repo.enrollments, state=ENROLLMENT_STATE.DROPPED)

        assert all(enrollment.state == ENROLLMENT_STATE.DROPPED for enrollment in new_enrollments)
        assert all(enrollment.state == ENROLLMENT_STATE.DROPPED for enrollment in repo.enrollments)


    def test_create_activity(self):
        repo = ActivityRepositoryMock()
        len_before = len(repo.activities)
        activity = repo.create_activity(
            Activity(
                code="newCode",
                title="Atividade da CAFE",
                description="Atividade pra tomar café",
                activity_type=ACTIVITY_TYPE.ALUMNI_CAFE,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 21, 19, 16, 52, 998305),
                duration=20,
                link=None,
                place="H332",
                responsible_professors=[
                    User(name="Rodrigo Santos", role=ROLE.PROFESSOR, user_id="b2f1")
                ],
                speakers=[
                    Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")
                ],
                total_slots=2,
                taken_slots=2,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=None
            )
        )
        assert type(activity) == Activity
        assert len(repo.activities) == len_before + 1

    def test_get_users(self):
        repo = ActivityRepositoryMock()
        users = repo.get_users(["12mf", "d7f1"])
        assert type(users) == list
        assert all(type(user) == User for user in users)
        assert len(users) == 2

