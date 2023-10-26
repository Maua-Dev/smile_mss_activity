import os
from datetime import datetime

import pytest

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.activity_repository_dynamo import ActivityRepositoryDynamo
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ActivityRepositoryDynamo:
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_all_activities_admin(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        activities_with_enrollments = activity_repository_dynamo.get_all_activities_admin()
        expected_activities_with_enrollments = activity_repository_mock.get_all_activities_admin()

        for activity_with_enrollments in activities_with_enrollments:
            activity_with_enrollments[1].sort(key=lambda x: x.user_id)

        for expected_activity_with_enrollments in expected_activities_with_enrollments:
            expected_activity_with_enrollments[1].sort(key=lambda x: x.user_id)

        activities_with_enrollments.sort(key=lambda x: x[0].code)
        expected_activities_with_enrollments.sort(key=lambda x: x[0].code)

        assert expected_activities_with_enrollments == activities_with_enrollments

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_all_activities(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        activities = activity_repository_dynamo.get_all_activities()
        expected_activities = activity_repository_mock.activities

        activities.sort(key=lambda x: x.code)
        expected_activities.sort(key=lambda x: x.code)

        assert expected_activities == activities


    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_activity(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        new_activity = new_activity = Activity(
            code="EAD109",
            title="Curso de verão de cálculo 2",
            description="curso de verão",
            activity_type=ACTIVITY_TYPE.COURSES,
            is_extensive=False,
            delivery_model=DELIVERY_MODEL.ONLINE,
            start_date=1671747413000,
            end_date=1671754613000,
            link=None,
            place="H332",
            responsible_professors=[
                User(name="Juliana Vetores", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="João Vitor Branco", bio="Incrível", company="IMT")],
            total_slots=4,
            taken_slots=4,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=1671743812000
        )

        activity_created = activity_repository_dynamo.create_activity(new_activity)

        assert activity_created == new_activity

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_activity(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        for activity in activity_repository_mock.activities:
            activity_gotten = activity_repository_dynamo.get_activity(activity.code)
            assert type(activity_gotten) == Activity
            assert activity_gotten.code == activity.code
            assert activity_gotten.title == activity.title
            assert activity_gotten.description == activity.description
            assert activity_gotten.delivery_model == activity.delivery_model
            assert activity_gotten.activity_type == activity.activity_type
            assert activity_gotten.start_date == activity.start_date
            assert activity_gotten.end_date == activity.end_date
            assert activity_gotten.link == activity.link
            assert activity_gotten.place == activity.place
            assert activity_gotten.responsible_professors == activity.responsible_professors
            assert activity_gotten.speakers == activity.speakers
            assert activity_gotten.total_slots == activity.total_slots
            assert activity_gotten.taken_slots == activity.taken_slots
            assert activity_gotten.accepting_new_enrollments == activity.accepting_new_enrollments
            assert activity_gotten.stop_accepting_new_enrollments_before == activity.stop_accepting_new_enrollments_before

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_activity_not_found(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()

        activity_gotten = activity_repository_dynamo.get_activity("SEM_CODIGO")

        assert activity_gotten is None

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_enrollment(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        enrollment = activity_repository_mock.enrollments[0]

        new_enrollment = activity_repository_dynamo.create_enrollment(enrollment)

        assert enrollment == new_enrollment

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_enrollment(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        enrollment = activity_repository_mock.enrollments[0]

        enrollment_gotten = activity_repository_dynamo.get_enrollment(enrollment.user_id, enrollment.activity_code)

        assert enrollment_gotten == enrollment

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_enrollment_dropped(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        enrollment = activity_repository_mock.enrollments[8]

        enrollment_gotten = activity_repository_dynamo.get_enrollment(enrollment.user_id, enrollment.activity_code)

        assert enrollment_gotten is None

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_enrollment_drop(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()
        enrollment = repo_activity_dynamo.update_enrollment(user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002", code="ECM2345",
                                            new_state=ENROLLMENT_STATE.DROPPED)

        assert enrollment.user_id == "d61dbf66-a10f-11ed-a8fc-0242ac120002"
        assert enrollment.activity_code == "ECM2345"
        assert enrollment.state == ENROLLMENT_STATE.DROPPED

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_enrollment_enroll(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        enrollment = repo_activity_dynamo.update_enrollment(user_id="03555872-a110-11ed-a8fc-0242ac120002", code="ECM2345",
                                            new_state=ENROLLMENT_STATE.ENROLLED)

        assert enrollment.user_id == "03555872-a110-11ed-a8fc-0242ac120002"
        assert enrollment.activity_code == "ECM2345"
        assert enrollment.state == ENROLLMENT_STATE.ENROLLED

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_enrollment_not_found(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        enrollment = repo_activity_dynamo.update_enrollment(user_id="03555872-a110-11ed-a8fc-0242ac120002", code="NAO_EXISTE", new_state=ENROLLMENT_STATE.DROPPED)

        assert enrollment is None

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_activity(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        repo_activity_dynamo = ActivityRepositoryDynamo()
        new_activity = repo_activity_dynamo.update_activity(code="PINOQ1",
                                                             new_title="NOVO TITULO",
                                                             new_description='nova descricao',
                                                             new_activity_type=ACTIVITY_TYPE.LECTURES,
                                                             new_is_extensive=True,
                                                             new_delivery_model=DELIVERY_MODEL.ONLINE,
                                                             new_start_date=1630465200000, new_end_date=1630466100000,
                                                             new_link="www.google.com.br",
                                                             new_place="Sala 1",
                                                             new_responsible_professors=[
                                                                 repo_user.users[2],
                                                                 repo_user.users[10]],
                                                             new_speakers=[
                                                                 Speaker(
                                                                     name="Fulano de Tal",
                                                                     bio="Fulano de Tal é um professor de Engenharia de Software",
                                                                     company="Universidade Federal de Fulano de tal",
                                                                 )
                                                             ], new_total_slots=100,
                                                             new_accepting_new_enrollments=True,
                                                            new_taken_slots=repo_activity.activities[0].taken_slots,
                                                             new_stop_accepting_new_enrollments_before=None)

        assert new_activity.code == "PINOQ1"
        assert new_activity.title == "NOVO TITULO"
        assert new_activity.description == 'nova descricao'
        assert new_activity.activity_type == ACTIVITY_TYPE.LECTURES
        assert new_activity.is_extensive == True
        assert new_activity.delivery_model == DELIVERY_MODEL.ONLINE
        assert new_activity.start_date == 1630465200000
        assert new_activity.end_date == 1630466100000
        assert new_activity.link == 'www.google.com.br'
        assert new_activity.place == "Sala 1"
        assert new_activity.responsible_professors == [
            repo_user.users[2],
            repo_user.users[10]]
        assert new_activity.speakers == [
            Speaker(
                name="Fulano de Tal",
                bio="Fulano de Tal é um professor de Engenharia de Software",
                company="Universidade Federal de Fulano de tal",
            )
        ]
        assert new_activity.total_slots == 100
        assert new_activity.accepting_new_enrollments == True
        assert new_activity.stop_accepting_new_enrollments_before == 1669918612000
        assert new_activity.taken_slots == repo_activity.activities[0].taken_slots


    @pytest.mark.skip("Can't test dynamo in Github")
    def test_delete_activity(self):
        repo_activity = ActivityRepositoryMock()
        activity = repo_activity.activities[3]

        repo_activity_dynamo = ActivityRepositoryDynamo()
        deleted_activity = repo_activity_dynamo.delete_activity(code=activity.code)

        assert activity == deleted_activity

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_activity_with_enrollments(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()
        activity, enrollments = repo_activity_dynamo.get_activity_with_enrollments("COD1468")

        assert type(activity) == Activity
        assert type(enrollments) == list

        assert all(type(enrollment) == Enrollment for enrollment in enrollments)
        assert len(enrollments) == 2

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_activity_with_enrollments_not_found(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()
        activity, enrollments = repo_activity_dynamo.get_activity_with_enrollments("SEM_CODIGO")

        assert activity is None
        assert enrollments is None

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_batch_update_enrollment(self):
        repo_activity_mock = ActivityRepositoryMock()

        enrollments_to_update = [repo_activity_mock.enrollments[10], repo_activity_mock.enrollments[11], repo_activity_mock.enrollments[12]]

        repo_activity_dynamo = ActivityRepositoryDynamo()

        new_enrollments = repo_activity_dynamo.batch_update_enrollment(enrollments_to_update, ENROLLMENT_STATE.ACTIVITY_CANCELLED)

        expected_new_enrollments = list()
        for enrollment in enrollments_to_update:
            assert enrollment.state == ENROLLMENT_STATE.ACTIVITY_CANCELLED
            expected_new_enrollments.append(enrollment)

        expected_new_enrollments.sort(key=lambda enrollment: enrollment.user_id)

        new_enrollments.sort(key=lambda enrollment: enrollment.user_id)

        assert new_enrollments == expected_new_enrollments

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_enrollments_by_user_id(self):
        repo_activity = ActivityRepositoryMock()

        repo_activity_dynamo = ActivityRepositoryDynamo()
        repo_user = UserRepositoryMock()

        expected_enrollments = repo_activity.get_enrollments_by_user_id(repo_user.users[0].user_id)

        enrollments = repo_activity_dynamo.get_enrollments_by_user_id(repo_user.users[0].user_id)
        expected_enrollments.sort(key=lambda enrollment: enrollment.activity_code)
        enrollments.sort(key=lambda enrollment: enrollment.activity_code)

        assert len(enrollments) == len(expected_enrollments)
        assert all(type(enrollment) == Enrollment for enrollment in enrollments)
        assert all(enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE for enrollment in enrollments)
        assert enrollments == expected_enrollments

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_all_activities_logged(self):
        repo_activity = ActivityRepositoryMock()

        repo_activity_dynamo = ActivityRepositoryDynamo()
        repo_user = UserRepositoryMock()

        activities, user_enrollments = repo_activity_dynamo.get_all_activities_logged(repo_user.users[4].user_id)

        expected_activities, expected_enrollments = repo_activity.get_all_activities_logged(repo_user.users[4].user_id)

        expected_activities.sort(key=lambda activity: activity.code)
        activities.sort(key=lambda activity: activity.code)
        expected_enrollments.sort(key=lambda enrollment: enrollment.activity_code)
        user_enrollments.sort(key=lambda enrollment: enrollment.activity_code)

        assert len(activities) == len(expected_activities)
        assert all(type(activity) == Activity for activity in activities)
        assert activities == expected_activities

        assert len(user_enrollments) == len(expected_enrollments)
        assert all(type(enrollment) == Enrollment for enrollment in user_enrollments)
        assert user_enrollments == expected_enrollments

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_all_activities_logged_no_enrollments(self):
        repo_activity = ActivityRepositoryMock()

        repo_activity_dynamo = ActivityRepositoryDynamo()
        repo_user = UserRepositoryMock()

        activities, user_enrollments = repo_activity_dynamo.get_all_activities_logged(repo_user.users[12].user_id)

        expected_activities, expected_enrollments = repo_activity.get_all_activities_logged(repo_user.users[12].user_id)

        expected_activities.sort(key=lambda activity: activity.code)
        activities.sort(key=lambda activity: activity.code)
        expected_enrollments.sort(key=lambda enrollment: enrollment.activity_code)
        user_enrollments.sort(key=lambda enrollment: enrollment.activity_code)

        assert len(activities) == len(expected_activities)
        assert all(type(activity) == Activity for activity in activities)
        assert activities == expected_activities

        assert len(user_enrollments) == len(expected_enrollments)
        assert all(type(enrollment) == Enrollment for enrollment in user_enrollments)
        assert user_enrollments == expected_enrollments


    @pytest.mark.skip("Can't test ses in Github")
    def test_send_enrolled_email(self):

        repo_activity_dynamo = ActivityRepositoryDynamo()
        repo_actiivty_mock = ActivityRepositoryMock()

        user = UserInfo(
            name="Vitor Soller",
            email="vgsoller@gmail.com",
            accepted_notifications_email=True,
            user_id="0"*36,
            phone=None,
            accepted_notifications_sms=False,
            role=ROLE.STUDENT
        )

        activity = repo_actiivty_mock.activities[0]

        confirmation = repo_activity_dynamo.send_enrolled_email(user, activity)

        assert confirmation

    @pytest.mark.skip("Can't test ses in Github")
    def test_send_deleted_user_email(self):

        repo_activity_dynamo = ActivityRepositoryDynamo()

        user = UserInfo(
            name="Vitor Soller",
            email="vgsoller@gmail.com",
            accepted_notifications_email=True,
            user_id="0"*36,
            phone=None,
            accepted_notifications_sms=False,
            role=ROLE.STUDENT
        )

        send_email = repo_activity_dynamo.send_deleted_user_email(user)

        assert send_email

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_delete_enrollment(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        repo_activity_dynamo.delete_enrollment(user_id="e51d5fd4-b509-4338-a029-ee5f0372968d", code="SOSTECNOLOGIA")

        assert True


    @pytest.mark.skip("Can't test s3 in Github")
    def test_delete_certificates(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        repo_activity_dynamo.delete_certificates(email="vgsoller@gmail.com")

        assert True

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_enrollments_by_user_id_with_dropped(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        enrollments = repo_activity_dynamo.get_enrollments_by_user_id_with_dropped("e51d5fd4-b509-4338-a029-ee5f0372968d")

        assert len(enrollments) == 33
        assert all(type(enrollment) == Enrollment for enrollment in enrollments)

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_activity_only_description(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        repo_activity_dynamo.update_activity(code="CODIGO", new_description="abuble")

        assert True

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_activity_only_taken_slots(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()
        
        repo_activity_dynamo.update_activity(code="CODIGO", new_taken_slots=2)
        repo_activity_dynamo.update_activity(code="ULTIMA", new_taken_slots=3)

        assert True
    
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_activity_only_responsible_professors(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()
        user_repository_mock = UserRepositoryMock()

        repo_activity_dynamo.update_activity(code="PRF246", new_responsible_professors=[user_repository_mock.users[9], user_repository_mock.users[2]])

        assert True
    
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_activity_only_speakers(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        repo_activity_dynamo.update_activity(code="ULTIMA", new_speakers=[Speaker(name="Fulano de Tal", bio="Fulano de Tal é um professor de Engenharia de Software", company="Universidade Federal de Fulano de tal")])

        assert True
    
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_batch_get_activities(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()
        repo_activity_mock = ActivityRepositoryMock()

        mock_activities = repo_activity_mock.batch_get_activities(["CODIGO", "ULTIMA"])

        activities = repo_activity_dynamo.batch_get_activities(["CODIGO", "ULTIMA"])

        assert len(activities) == 2
        assert all(type(activity) == Activity for activity in activities)

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_activity_with_enrollments_sort(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()
        repo_user = UserRepositoryMock()


        enrollment1 = Enrollment(activity_code='2468', user_id=repo_user.users[7].user_id, state=ENROLLMENT_STATE.COMPLETED,    
                                date_subscribed=1671229013000)
        enrollment2 = Enrollment(activity_code='2468', user_id=repo_user.users[8].user_id, state=ENROLLMENT_STATE.COMPLETED,
                                    date_subscribed=1670229013000)
        enrollment3 = Enrollment(activity_code='2468', user_id=repo_user.users[0].user_id, state=ENROLLMENT_STATE.ENROLLED,
                                    date_subscribed=1671229013000)
        enrollment4 = Enrollment(activity_code='2468', user_id=repo_user.users[1].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                                    date_subscribed=1670229013000)  

        # repo_activity_dynamo.create_enrollment(enrollment1)
        # repo_activity_dynamo.create_enrollment(enrollment2)
        # repo_activity_dynamo.create_enrollment(enrollment3)	
        # repo_activity_dynamo.create_enrollment(enrollment4)

        activity, enrollments = repo_activity_dynamo.get_activity_with_enrollments("2468")

        assert enrollments[0] == enrollment2
        assert enrollments[1] == enrollment1
        assert enrollments[2] == enrollment4
        assert enrollments[3] == enrollment3
    
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_batch_delete_enrollments(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        activity, enrollments = repo_activity_dynamo.get_activity_with_enrollments("SC456")

        deleted_enrollments = repo_activity_dynamo.batch_delete_enrollments([enrollment.user_id for enrollment in enrollments], activity.code)

        assert True

    def test_get_all_activitites_logged_positions(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()
        repo_user = UserRepositoryMock()
        repo = ActivityRepositoryMock()

        enrollment1 = Enrollment(activity_code='AC000', user_id=repo_user.users[2].user_id, state=ENROLLMENT_STATE.IN_QUEUE,    
                                    date_subscribed=1671229013000)
        
        enrollment2 = Enrollment(activity_code='AC000', user_id=repo_user.users[2].user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                                    date_subscribed=1669229013000) 
        repo.enrollments.append(enrollment1)
        repo.enrollments.append(enrollment2)

        activities, user_enrollments = repo_activity_dynamo.get_all_activities_logged(repo_user.users[2].user_id)

        # repo_activity_dynamo.create_enrollment(enrollment1)
        # repo_activity_dynamo.create_enrollment(enrollment2)

        expected_activities, expected_enrollments = repo_activity_dynamo.get_all_activities_logged(repo_user.users[2].user_id)

        assert len(activities) == len(expected_activities)
        assert all(type(activity) == Activity for activity in activities)
        assert activities == expected_activities

        assert len(user_enrollments) == len(expected_enrollments)
        assert all(type(enrollment) == Enrollment for enrollment in user_enrollments)
        assert user_enrollments == expected_enrollments

        assert user_enrollments[len(user_enrollments)-2].position == 1
        assert user_enrollments[len(user_enrollments)-1].position == 2

        assert expected_enrollments[len(expected_enrollments)-2].position == 1
        assert expected_enrollments[len(expected_enrollments)-1].position == 2

    