from src.modules.get_enrollments_by_user.app.get_enrollments_by_user_usecase import GetEnrollmentsByUserUsecase
from src.modules.get_enrollments_by_user.app.get_enrollments_by_user_viewmodel import \
    GetEnrollmentsByUserViewmodel
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="get_enrollments_by_user")

class Test_GetEnrollmentsByUserViewmodel:

    def test_get_enrollments_by_user_viewmodel(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetEnrollmentsByUserUsecase(repo, observability=observability)

        list_enrollments = usecase(user_id=repo_user.users[1].user_id)

        viewmodel = GetEnrollmentsByUserViewmodel(list_enrollments, repo_user.users[1])

        expected = {
            'enrollments': [
                {
                    'activity_code': 'ECM2345',
                    'state': 'ENROLLED',
                    'date_subscribed': 1671315413000
                },
                {
                    'activity_code': 'ELET355',
                    'state': 'ENROLLED',
                    'date_subscribed': 1671488213000
                },
                {
                    'activity_code': 'CAFE',
                    'state': 'ENROLLED',
                    'date_subscribed': 1671488213000
                },
                {
                    'activity_code': 'ULTIMA',
                    'state': 'ENROLLED',
                    'date_subscribed': 1670710613000
                }
            ],
            'user': {
                'name': 'Bruno Soller',
                'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                'role': 'STUDENT'
            },
            'message': 'the enrollments were retrieved'
        }

        assert viewmodel.to_dict() == expected

    def test_get_enrollments_by_user_viewmodel_zero_enrollments(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetEnrollmentsByUserUsecase(repo, observability=observability)

        list_enrollments = usecase(user_id=repo_user.users[11].user_id)

        viewmodel = GetEnrollmentsByUserViewmodel(list_enrollments, repo_user.users[11])

        expected = {
            'enrollments': [

            ],
            'user': {
                'name': 'Rafael Santos',
                'user_id': '62cafdd4-a110-11ed-a8fc-0242ac120002',
                'role': 'PROFESSOR'
            },
            'message': 'the enrollments were retrieved'
        }

        assert viewmodel.to_dict() == expected

    def test_get_enrollments_by_user_viewmodel_with_in_queue(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetEnrollmentsByUserUsecase(repo, observability=observability)

        list_enrollments = usecase(user_id=repo_user.users[4].user_id)

        viewmodel = GetEnrollmentsByUserViewmodel(list_enrollments, repo_user.users[4])

        expected = {
            'enrollments': [
                {
                    'activity_code': 'ECM2345',
                    'state': 'IN_QUEUE',
                    'date_subscribed': 1671574613000
                },
                {
                    'activity_code': 'COD1468',
                    'state': 'ENROLLED',
                    'date_subscribed': 1671488213000
                },
                {
                    'activity_code': 'ULTIMA',
                    'state': 'IN_QUEUE',
                    'date_subscribed': 1671661013000
                },
                {
                    'activity_code': 'PINOQ1',
                    'state': 'ENROLLED',
                    'date_subscribed': 1669760213000
                }
            ],
            'user': {
                'name': 'Hector Guerrini',
                'user_id': '03555872-a110-11ed-a8fc-0242ac120002',
                'role': 'EXTERNAL'
            },
            'message': 'the enrollments were retrieved'
        }

        assert viewmodel.to_dict() == expected
