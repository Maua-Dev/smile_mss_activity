from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from freezegun import freeze_time


class Test_DeleteUserUsecase:

    def test_delete_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        delete_user_usecase = DeleteUserUsecase(repo_activity, repo_user)

        user_info = repo_user.users[13]

        len_before = len(repo_user.users)

        user = User(
            user_id=user_info.user_id,
            name=user_info.name,
            role=user_info.role
        )

        user = delete_user_usecase(user)

        assert len_before == len(repo_user.users) + 1
        assert type(user) == UserInfo

    def test_delete_user_enrolled_activities(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        delete_user_usecase = DeleteUserUsecase(repo_activity, repo_user)

        user_info = repo_user.users[13]

        user = User(
            user_id=user_info.user_id,
            name=user_info.name,
            role=user_info.role
        )
        activity_12 = repo_activity.activities[12]
        activity_1 = repo_activity.activities[1]

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_12.code,
                state=ENROLLMENT_STATE.IN_QUEUE,
                date_subscribed=1669760213000
            )
        )

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_1.code,
                state=ENROLLMENT_STATE.ENROLLED,
                date_subscribed=1669760213000
            )
        )


        users_len_before = len(repo_user.users)
        enrollments_len_before = len(repo_activity.enrollments)

        user = delete_user_usecase(user)

        assert users_len_before == len(repo_user.users) + 1
        assert enrollments_len_before == len(repo_activity.enrollments) + 2
        assert type(user) == UserInfo


    @freeze_time("2022-12-20")
    def test_delete_user_enrolled_activities_with_queue(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        delete_user_usecase = DeleteUserUsecase(repo_activity, repo_user)

        user_info = repo_user.users[13]

        user = User(
            user_id=user_info.user_id,
            name=user_info.name,
            role=user_info.role
        )

        activity_12 = repo_activity.activities[12]
        activity_1 = repo_activity.activities[1]
        repo_activity.activities[0].total_slots = 5
        repo_activity.activities[0].taken_slots = 5
        activity_0 = repo_activity.activities[0]

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_12.code,
                state=ENROLLMENT_STATE.DROPPED,
                date_subscribed=1669760213000
            )
        )

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_1.code,
                state=ENROLLMENT_STATE.ENROLLED,
                date_subscribed=1669760213000
            )
        )

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_0.code,
                state=ENROLLMENT_STATE.ENROLLED,
                date_subscribed=1671550100000
            )
        )


        repo_user.users.append(user)

        users_len_before = len(repo_user.users)
        enrollments_len_before = len(repo_activity.enrollments)

        user = delete_user_usecase(user)

        ex_queue_enrollment_state = repo_activity.enrollments[4].state

        assert users_len_before == len(repo_user.users) + 1
        assert enrollments_len_before == len(repo_activity.enrollments) + 3
        assert type(user) == UserInfo
        assert ex_queue_enrollment_state == ENROLLMENT_STATE.ENROLLED


    def test_delete_user_enrolled_activities_with_queue_activity_already_started(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        delete_user_usecase = DeleteUserUsecase(repo_activity, repo_user)

        user_info = repo_user.users[13]

        user = User(
            user_id=user_info.user_id,
            name=user_info.name,
            role=user_info.role
        )

        activity_12 = repo_activity.activities[12]
        activity_1 = repo_activity.activities[1]
        repo_activity.activities[0].total_slots = 5
        repo_activity.activities[0].taken_slots = 5
        activity_0 = repo_activity.activities[0]

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_12.code,
                state=ENROLLMENT_STATE.DROPPED,
                date_subscribed=1669760213000
            )
        )

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_1.code,
                state=ENROLLMENT_STATE.ENROLLED,
                date_subscribed=1669760213000
            )
        )

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_0.code,
                state=ENROLLMENT_STATE.ENROLLED,
                date_subscribed=1671550100000
            )
        )

        repo_user.users.append(user)

        users_len_before = len(repo_user.users)
        enrollments_len_before = len(repo_activity.enrollments)

        user = delete_user_usecase(user)

        still_queue_enrollment = repo_activity.enrollments[4].state

        assert users_len_before == len(repo_user.users) + 1
        assert enrollments_len_before == len(repo_activity.enrollments) + 3
        assert type(user) == UserInfo
        assert still_queue_enrollment == ENROLLMENT_STATE.IN_QUEUE


    @freeze_time("2022-12-20")
    def test_delete_user_enrolled_activities_in_queue_with_queue(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        delete_user_usecase = DeleteUserUsecase(repo_activity, repo_user)

        user_info = repo_user.users[13]

        user = User(
            user_id=user_info.user_id,
            name=user_info.name,
            role=user_info.role
        )

        activity_12 = repo_activity.activities[12]
        activity_0 = repo_activity.activities[0]

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_12.code,
                state=ENROLLMENT_STATE.DROPPED,
                date_subscribed=1669760213000
            )
        )

        repo_activity.enrollments.append(
            Enrollment(
                user_id=user.user_id,
                activity_code=activity_0.code,
                state=ENROLLMENT_STATE.IN_QUEUE,
                date_subscribed=1671550100000
            )
        )

        repo_user.users.append(user)

        users_len_before = len(repo_user.users)
        enrollments_len_before = len(repo_activity.enrollments)

        user = delete_user_usecase(user)

        still_queue_enrollment = repo_activity.enrollments[4].state

        assert users_len_before == len(repo_user.users) + 1
        assert enrollments_len_before == len(repo_activity.enrollments) + 2
        assert type(user) == UserInfo
        assert still_queue_enrollment == ENROLLMENT_STATE.IN_QUEUE




