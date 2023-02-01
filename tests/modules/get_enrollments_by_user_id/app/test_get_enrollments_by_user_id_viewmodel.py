from src.modules.get_enrollments_by_user_id.app.get_enrollments_by_user_id_usecase import GetEnrollmentsByUserIdUsecase
from src.modules.get_enrollments_by_user_id.app.get_enrollments_by_user_id_viewmodel import \
    GetEnrollmentsByUserIdViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetEnrollmentsByUserId:

    def test_get_enrollments_by_user_id_viewmodel(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentsByUserIdUsecase(repo)

        list_enrollments = usecase(user_id=repo.users[1].user_id)

        viewmodel = GetEnrollmentsByUserIdViewmodel(list_enrollments)

        expected = {
            'enrollments': [
                {
                    'activity_code': 'ECM2345',
                    'user': {
                        'name': 'Bruno Soller',
                        'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                        'role': 'STUDENT'
                    },
                    'state': 'ENROLLED',
                    'date_subscribed': 1671315413000
                },
                {
                    'activity_code': 'ELET355',
                    'user': {
                        'name': 'Bruno Soller',
                        'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                        'role': 'STUDENT'
                    },
                    'state': 'ENROLLED',
                    'date_subscribed': 1671488213000
                },
                {
                    'activity_code': 'CAFE',
                    'user': {
                        'name': 'Bruno Soller',
                        'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                        'role': 'STUDENT'
                    },
                    'state': 'ENROLLED',
                    'date_subscribed': 1671488213000
                },
                {
                    'activity_code': 'ULTIMA',
                    'user': {
                        'name': 'Bruno Soller',
                        'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                        'role': 'STUDENT'
                    },
                    'state': 'ENROLLED',
                    'date_subscribed': 1670710613000
                }
            ],
            'message': "the enrollments were retrieved"
        }

        assert viewmodel.to_dict() == expected

    def test_get_enrollments_by_user_id_viewmodel_zero_enrollments(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentsByUserIdUsecase(repo)

        list_enrollments = usecase(user_id=repo.users[11].user_id)

        viewmodel = GetEnrollmentsByUserIdViewmodel(list_enrollments)

        expected = {
            'enrollments': [

            ],
            'message': 'the enrollments were retrieved'
        }

        assert viewmodel.to_dict() == expected
