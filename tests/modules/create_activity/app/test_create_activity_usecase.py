import datetime

import pytest
from src.modules.create_activity.app.create_activity_usecase import CreateActivityUsecase
from src.shared.domain.entities import speaker
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError

class Test_CreateActivityUsecase:

        def test_create_activity_user(self):
                repo = ActivityRepositoryMock()
                usecase = CreateActivityUsecase(repo)
                activitiesLenBefore = len(repo.activities)

                activity = usecase(code="CodigoNovo",title="Atividade da ECM 2345",  description="Isso é uma atividade", 
                                duration=120, link=None, place="H332", total_slots=4, is_extensive=True, taken_slots=4, accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES, delivery_model=DELIVERY_MODEL.HYBRID,start_date=datetime.datetime(2022, 12, 22, 19, 16, 52, 998305), 
                                stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 18, 16, 52, 998305), speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")], responsible_professors=[User(name="Rafael Santos", role=ROLE.PROFESSOR, user_id="12mf")])


                activitiesLenAfter = activitiesLenBefore + 1 

                assert len(repo.activities) == activitiesLenAfter
                assert repo.activities[activitiesLenBefore].code == "CodigoNovo"
                assert repo.activities[activitiesLenBefore].title == "Atividade da ECM 2345"
                assert repo.activities[activitiesLenBefore].description == "Isso é uma atividade"
                assert repo.activities[activitiesLenBefore].activity_type == ACTIVITY_TYPE.LECTURES
               # assert repo.activities[activitiesLenBefore].is_extensive == False
               # assert repo.activities[activitiesLenBefore].delivery_model == DELIVERY_MODEL.IN_PERSON
               # assert repo.activities[activitiesLenBefore].start_date == datetime.datetime(2022, 12, 22, 19, 16, 52, 998305)
               # assert repo.activities[activitiesLenBefore].duration == 120
               # assert repo.activities[activitiesLenBefore].link == None
               # assert repo.activities[activitiesLenBefore].place == "H332"
               # assert repo.activities[activitiesLenBefore].responsible_professors == [self.users[2]]
               # assert repo.activities[activitiesLenBefore].speakers == [self.speakers[0]]
               # assert repo.activities[activitiesLenBefore].total_slots == 4
               # assert repo.activities[activitiesLenBefore].taken_slots == 4
               # assert repo.activities[activitiesLenBefore].accepting_new_enrollments == True
               # assert repo.activities[activitiesLenBefore].stop_accepting_new_enrollments_before == datetime.datetime(2022, 12, 22, 18, 16, 52, 998305)
               # assert repo.activities["code"] == activity

        def test_create_activity_usecase_invalid_code_int(self):
                repo = ActivityRepositoryMock()
                usecase = CreateActivityUsecase(repo=repo)

                with pytest.raises(EntityError):
                        usecase(code = 00000,title="Atividade da ECM 2345",  description="Isso é uma atividade", 
                                duration=120, link=None, place="H332", total_slots=4, is_extensive=True, taken_slots=4, accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES, delivery_model=DELIVERY_MODEL.HYBRID,start_date=datetime.datetime(2022, 12, 22, 19, 16, 52, 998305), 
                                stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 18, 16, 52, 998305), speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")], responsible_professors=[User(name="Rafael Santos", role=ROLE.PROFESSOR, user_id="12mf")])

        def test_create_activity_usecase_not_str(self):
                repo = ActivityRepositoryMock()
                usecase = CreateActivityUsecase(repo=repo)

                with pytest.raises(EntityError):
                        usecase(code = 123, title="Atividade da ECM 2345",  description="Isso é uma atividade", 
                                duration=120, link=None, place="H332", total_slots=4, is_extensive=True, taken_slots=4, accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES, delivery_model=DELIVERY_MODEL.HYBRID,start_date=datetime.datetime(2022, 12, 22, 19, 16, 52, 998305), 
                                stop_accepting_new_enrollments_before=datetime.datetime(2022, 12, 22, 18, 16, 52, 998305), speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")], responsible_professors=[User(name="Rafael Santos", role=ROLE.PROFESSOR, user_id="12mf")])