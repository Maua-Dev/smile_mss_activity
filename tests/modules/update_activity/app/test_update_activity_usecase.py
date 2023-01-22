import datetime
import pytest

from src.modules.update_activity.app.update_activity_usecase import UpdateActivityUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError

class Test_UpdateActivityUsecase:

       def test_update_activity(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)
              update_activity = usecase(code=repo.activities[0].code, new_description='nova descricao')

              assert type(update_activity) == Activity
              assert repo.activities[0].description == update_activity.description

       def test_update_activity_enum(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)
              update_activity = usecase(code=repo.activities[0].code, new_activity_type="LECTURES", new_delivery_model="HYBRID")

              assert type(update_activity) == Activity
              assert repo.activities[0].activity_type == update_activity.activity_type
              assert repo.activities[0].delivery_model == update_activity.delivery_model

       def test_update_activity_title_taken_slots(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)
              update_activity = usecase(code=repo.activities[0].code, new_title='NOVO TITULO', new_taken_slots=40)

              assert type(update_activity) == Activity
              assert repo.activities[0].title == update_activity.title
              assert repo.activities[0].taken_slots == update_activity.taken_slots

       def test_update_activity_invalid_code(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(555)

       def test_update_activity_invalid_new_title(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_title=123)

       def test_update_activity_invalid_new_description(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_description=456)

       def test_update_activity_invalid_new_activity_type(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_activity_type='TYPE_ERROR')

       def test_update_activity_invalid_new_is_extensive(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_is_extensive='NAO EH')

       def test_update_activity_invalid_new_delivery_model(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_delivery_model=000)

       def test_update_activity_invalid_new_start_date(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_start_date='AGORA')

       def test_update_activity_invalid_new_duration(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_duration='1500 minutos')

       def test_update_activity_invalid_new_responsible_professors(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_responsible_professors=repo.speakers[0])

       def test_update_activity_invalid_new_speakers(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_speakers=repo.users[5])

       def test_update_activity_invalid_new_total_slots(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_total_slots='500')

       def test_update_activity_invalid_new_taken_slots(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_taken_slots='1')
       
       def test_update_activity_invalid_new_accepting_new_enrollments(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_accepting_new_enrollments='NAO')

       def test_update_activity_invalid_new_stop_accepting_new_enrollments_before(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(EntityError):
                     update_activity = usecase(code='ELET355', new_stop_accepting_new_enrollments_before='DEPOIS DE AMANHA')
       
       def test_update_activity_is_none(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)

              with pytest.raises(NoItemsFound):
                     update_activity = usecase(code='')
       