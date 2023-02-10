from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class Test_UserApiGatewayDTO:

    def test_user_api_gateway_dto_to_entity(self):

        user_dto = UserApiGatewayDTO(
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            name="Vitor Soller",
            role=ROLE.ADMIN)

        user = user_dto.to_entity()

        expected_user = User(
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            name="Vitor Soller",
            role=ROLE.ADMIN)

        assert user == expected_user

    def test_user_api_gateway_dto_from_api_gateway(self):
        user_data = {'sub': 'd61dbf66-a10f-11ed-a8fc-0242ac120002', 'name': 'Vitor Soller', 'custom:role': 'ADMIN'}

        user_dto = UserApiGatewayDTO.from_api_gateway(user_data)

        expected_user_dto = UserApiGatewayDTO(
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            name="Vitor Soller",
            role=ROLE.ADMIN)

        assert user_dto == expected_user_dto

    def test_user_api_gateway_dto_from_api_gateway_to_entity(self):
        user_data = {'sub': 'd61dbf66-a10f-11ed-a8fc-0242ac120002', 'name': 'Vitor Soller', 'custom:role': 'ADMIN'}

        user_dto = UserApiGatewayDTO.from_api_gateway(user_data)

        user = user_dto.to_entity()

        expected_user = User(
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            name="Vitor Soller",
            role=ROLE.ADMIN)

        assert user == expected_user

