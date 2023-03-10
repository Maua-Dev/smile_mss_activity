import pytest

from src.modules.update_activity.app.update_activity_usecase import UpdateActivityUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateActivityUsecase:

    def test_update_activity(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)
        update_activity = usecase(code=repo_activity.activities[0].code, new_title="NOVO TITULO",
                                  new_description='nova descricao',
                                  new_activity_type=ACTIVITY_TYPE.LECTURES,
                                  new_is_extensive=True,
                                  new_delivery_model=DELIVERY_MODEL.ONLINE,
                                  new_start_date=1630465200000, new_duration=15,
                                  new_link="https://www.youtube.com/watch?v=1q2w3e4r5t6y7u8i9o0p",
                                  new_place="Sala 1",
                                  new_responsible_professors_user_id=[repo_user.users[2].user_id],
                                  new_speakers=[
                                      Speaker(
                                          name="Fulano de Tal",
                                          bio="Fulano de Tal é um professor de Engenharia de Software",
                                          company="Universidade Federal de Fulano de tal",
                                      )
                                  ], new_total_slots=100,
                                  new_accepting_new_enrollments=True,
                                  user=repo_user.users[0],
                                  new_stop_accepting_new_enrollments_before=None)

        assert type(update_activity) == Activity

        assert repo_activity.activities[0].title == update_activity.title
        assert repo_activity.activities[0].title == "NOVO TITULO"
        assert repo_activity.activities[0].description == update_activity.description
        assert repo_activity.activities[0].activity_type == update_activity.activity_type
        assert repo_activity.activities[0].is_extensive == update_activity.is_extensive
        assert repo_activity.activities[0].delivery_model == update_activity.delivery_model
        assert repo_activity.activities[0].start_date == update_activity.start_date
        assert repo_activity.activities[0].duration == update_activity.duration
        assert repo_activity.activities[0].link == update_activity.link
        assert repo_activity.activities[0].place == update_activity.place
        assert repo_activity.activities[0].responsible_professors == [repo_user.users[2]]
        assert repo_activity.activities[0].speakers == update_activity.speakers
        assert repo_activity.activities[0].total_slots == update_activity.total_slots
        assert repo_activity.activities[0].accepting_new_enrollments == update_activity.accepting_new_enrollments
        assert repo_activity.activities[
                   0].stop_accepting_new_enrollments_before == update_activity.stop_accepting_new_enrollments_before

    def test_update_activity_usecase_different_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)
        update_activity = usecase(code=repo_activity.activities[0].code, new_title="NOVO TITULO",
                                  new_description='nova descricao',
                                  new_activity_type=ACTIVITY_TYPE.LECTURES,
                                  new_is_extensive=True,
                                  new_delivery_model=DELIVERY_MODEL.ONLINE,
                                  new_start_date=1630465200000, new_duration=15,
                                  new_link="https://www.youtube.com/watch?v=1q2w3e4r5t6y7u8i9o0p",
                                  new_place="Sala 1",
                                  new_responsible_professors_user_id=[repo_user.users[11].user_id],
                                  new_speakers=[
                                      Speaker(
                                          name="Fulano de Tal",
                                          bio="Fulano de Tal é um professor de Engenharia de Software",
                                          company="Universidade Federal de Fulano de tal",
                                      )
                                  ], new_total_slots=100,
                                  new_accepting_new_enrollments=True,
                                  user=repo_user.users[0],
                                  new_stop_accepting_new_enrollments_before=None)

        assert type(update_activity) == Activity

        assert repo_activity.activities[0].title == update_activity.title
        assert repo_activity.activities[0].title == "NOVO TITULO"
        assert repo_activity.activities[0].description == update_activity.description
        assert repo_activity.activities[0].activity_type == update_activity.activity_type
        assert repo_activity.activities[0].is_extensive == update_activity.is_extensive
        assert repo_activity.activities[0].delivery_model == update_activity.delivery_model
        assert repo_activity.activities[0].start_date == update_activity.start_date
        assert repo_activity.activities[0].duration == update_activity.duration
        assert repo_activity.activities[0].link == update_activity.link
        assert repo_activity.activities[0].place == update_activity.place
        assert repo_activity.activities[0].responsible_professors == [repo_user.users[11]]
        assert repo_activity.activities[0].speakers == update_activity.speakers
        assert repo_activity.activities[0].total_slots == update_activity.total_slots
        assert repo_activity.activities[0].accepting_new_enrollments == update_activity.accepting_new_enrollments
        assert repo_activity.activities[
                   0].stop_accepting_new_enrollments_before == update_activity.stop_accepting_new_enrollments_before

    def test_update_activity_usecase_one_parameter(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)
        old_activity = repo_activity.activities[0]
        update_activity = usecase(code=repo_activity.activities[0].code,
                                  new_title="NOVO TITULO",
                                  new_description="Isso é uma atividade",
                                  new_activity_type=ACTIVITY_TYPE.COURSES,
                                  new_is_extensive=False,
                                  new_delivery_model=DELIVERY_MODEL.IN_PERSON,
                                  new_start_date=1671747413000,
                                  new_duration=120,
                                  new_link=None,
                                  new_place="H332",
                                  new_responsible_professors_user_id=["03555624-a110-11ed-a8fc-0242ac120002"],
                                  new_speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                                  new_total_slots=4,
                                  new_accepting_new_enrollments=True,
                                  user=repo_user.users[0],
                                  new_stop_accepting_new_enrollments_before=1671743812000)

        assert type(update_activity) == Activity

        assert repo_activity.activities[0].title == old_activity.title
        assert repo_activity.activities[0].description == old_activity.description
        assert repo_activity.activities[0].activity_type == old_activity.activity_type
        assert repo_activity.activities[0].activity_type == ACTIVITY_TYPE.COURSES
        assert repo_activity.activities[0].is_extensive == old_activity.is_extensive
        assert repo_activity.activities[0].delivery_model == old_activity.delivery_model
        assert repo_activity.activities[0].start_date == old_activity.start_date
        assert repo_activity.activities[0].duration == old_activity.duration
        assert repo_activity.activities[0].link == old_activity.link
        assert repo_activity.activities[0].place == old_activity.place
        assert repo_activity.activities[0].responsible_professors == old_activity.responsible_professors
        assert repo_activity.activities[0].speakers == old_activity.speakers
        assert repo_activity.activities[0].total_slots == old_activity.total_slots
        assert repo_activity.activities[0].accepting_new_enrollments == old_activity.accepting_new_enrollments
        assert repo_activity.activities[
                   0].stop_accepting_new_enrollments_before == old_activity.stop_accepting_new_enrollments_before

    def test_update_activity_new_activity_invalid_enum(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)
        with pytest.raises(EntityError):
            update_activity = usecase(code=repo_activity.activities[0].code, new_title="NOVO TITULO",
                                      new_description='nova descricao',
                                      new_activity_type="LECTURES",
                                      new_is_extensive=True,
                                      new_delivery_model=DELIVERY_MODEL.ONLINE,
                                      new_start_date=1630465200000, new_duration=15,
                                      new_link="https://www.youtube.com/watch?v=1q2w3e4r5t6y7u8i9o0p",
                                      new_place="Sala 1",
                                      new_responsible_professors_user_id=[repo_user.users[2].user_id,
                                                                          repo_user.users[11].user_id],
                                      new_speakers=[
                                          Speaker(
                                              name="Fulano de Tal",
                                              bio="Fulano de Tal é um professor de Engenharia de Software",
                                              company="Universidade Federal de Fulano de tal",
                                          )
                                      ], new_total_slots=100,
                                      new_accepting_new_enrollments=True,
                                      user=repo_user.users[0],
                                      new_stop_accepting_new_enrollments_before=None)

    def test_update_activity_invalid_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)

        with pytest.raises(EntityError):
            update_activity = usecase(code=555, new_title="NOVO TITULO", new_description='nova descricao',
                                      new_activity_type=ACTIVITY_TYPE.LECTURES,
                                      new_is_extensive=True,
                                      new_delivery_model=DELIVERY_MODEL.ONLINE,
                                      new_start_date=1630465200000, new_duration=15,
                                      new_link="https://www.youtube.com/watch?v=1q2w3e4r5t6y7u8i9o0p",
                                      new_place="Sala 1",
                                      new_responsible_professors_user_id=[repo_user.users[2].user_id,
                                                                          repo_user.users[11].user_id],
                                      new_speakers=[
                                          Speaker(
                                              name="Fulano de Tal",
                                              bio="Fulano de Tal é um professor de Engenharia de Software",
                                              company="Universidade Federal de Fulano de tal",
                                          )
                                      ], new_total_slots=100,
                                      new_accepting_new_enrollments=True,
                                      user=repo_user.users[0],
                                      new_stop_accepting_new_enrollments_before=None)

    def test_update_activity_invalid_title(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)

        with pytest.raises(EntityError):
            update_activity = usecase(code=repo_activity.activities[0].code, new_title=123, new_description='nova descricao',
                                      new_activity_type=ACTIVITY_TYPE.LECTURES,
                                      new_is_extensive=True,
                                      new_delivery_model=DELIVERY_MODEL.ONLINE,
                                      new_start_date=1630465200000, new_duration=15,
                                      new_link="https://www.youtube.com/watch?v=1q2w3e4r5t6y7u8i9o0p",
                                      new_place="Sala 1",
                                      new_responsible_professors_user_id=[repo_user.users[2].user_id,
                                                                          repo_user.users[11].user_id],
                                      new_speakers=[
                                          Speaker(
                                              name="Fulano de Tal",
                                              bio="Fulano de Tal é um professor de Engenharia de Software",
                                              company="Universidade Federal de Fulano de tal",
                                          )
                                      ], new_total_slots=100,
                                      new_accepting_new_enrollments=True,
                                      user=repo_user.users[0],
                                      new_stop_accepting_new_enrollments_before=None)

    def test_update_activity_is_not_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)

        with pytest.raises(NoItemsFound):
            update_activity = usecase(code=repo_activity.activities[0].code + "1", new_title="NOVO TITULO",
                                      new_description='nova descricao',
                                      new_activity_type=ACTIVITY_TYPE.LECTURES,
                                      new_is_extensive=True,
                                      new_delivery_model=DELIVERY_MODEL.ONLINE,
                                      new_start_date=1630465200000, new_duration=15,
                                      new_link="https://www.youtube.com/watch?v=1q2w3e4r5t6y7u8i9o0p",
                                      new_place="Sala 1",
                                      new_responsible_professors_user_id=[repo_user.users[2].user_id,
                                                                          repo_user.users[11].user_id],
                                      new_speakers=[
                                          Speaker(
                                              name="Fulano de Tal",
                                              bio="Fulano de Tal é um professor de Engenharia de Software",
                                              company="Universidade Federal de Fulano de tal",
                                          )
                                      ], new_total_slots=100,
                                      new_accepting_new_enrollments=True,
                                      user=repo_user.users[0],
                                      new_stop_accepting_new_enrollments_before=None)

    def test_update_activity_invalid_responsible_professors(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)

        with pytest.raises(EntityError):
            update_activity = usecase(code=repo_activity.activities[0].code, new_title="NOVO TITULO",
                                      new_description='nova descricao',
                                      new_activity_type=ACTIVITY_TYPE.LECTURES,
                                      new_is_extensive=True,
                                      new_delivery_model=DELIVERY_MODEL.ONLINE,
                                      new_start_date=1630465200000, new_duration=15,
                                      new_link="https://www.youtube.com/watch?v=1q2w3e4r5t6y7u8i9o0p",
                                      new_place="Sala 1",
                                      new_responsible_professors_user_id=[repo_user.users[2].user_id, repo_user.users[11].user_id,
                                                                          999],
                                      new_speakers=[
                                          Speaker(
                                              name="Fulano de Tal",
                                              bio="Fulano de Tal é um professor de Engenharia de Software",
                                              company="Universidade Federal de Fulano de tal",
                                          )
                                      ], new_total_slots=100,
                                      new_accepting_new_enrollments=True,
                                      user=repo_user.users[0],
                                      new_stop_accepting_new_enrollments_before=None)

    def test_update_activity_invalid_responsible_professors_not_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)

        with pytest.raises(NoItemsFound):
            update_activity = usecase(code=repo_activity.activities[0].code, new_title="NOVO TITULO",
                                      new_description='nova descricao',
                                      new_activity_type=ACTIVITY_TYPE.LECTURES,
                                      new_is_extensive=True,
                                      new_delivery_model=DELIVERY_MODEL.ONLINE,
                                      new_start_date=1630465200000, new_duration=15,
                                      new_link="https://www.youtube.com/watch?v=1q2w3e4r5t6y7u8i9o0p",
                                      new_place="Sala 1",
                                      new_responsible_professors_user_id=[repo_user.users[2].user_id, repo_user.users[11].user_id,
                                                                          "9999"],
                                      new_speakers=[
                                          Speaker(
                                              name="Fulano de Tal",
                                              bio="Fulano de Tal é um professor de Engenharia de Software",
                                              company="Universidade Federal de Fulano de tal",
                                          )
                                      ], new_total_slots=100,
                                      new_accepting_new_enrollments=True,
                                      user=repo_user.users[0],
                                      new_stop_accepting_new_enrollments_before=None)

    def test_update_activity_usecase_forbidden_requester_not_admin(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = UpdateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user)
        old_activity = repo_activity.activities[0]
        with pytest.raises(ForbiddenAction):
            update_activity = usecase(code=repo_activity.activities[0].code,
                                      new_title="NOVO TITULO",
                                      new_description="Isso é uma atividade",
                                      new_activity_type=ACTIVITY_TYPE.COURSES,
                                      new_is_extensive=False,
                                      new_delivery_model=DELIVERY_MODEL.IN_PERSON,
                                      new_start_date=1671747413000,
                                      new_duration=120,
                                      new_link=None,
                                      new_place="H332",
                                      new_responsible_professors_user_id=["03555624-a110-11ed-a8fc-0242ac120002"],
                                      new_speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
                                      new_total_slots=4,
                                      new_accepting_new_enrollments=True,
                                      user=repo_user.users[1],
                                      new_stop_accepting_new_enrollments_before=1671743812000)
