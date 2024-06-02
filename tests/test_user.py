import allure
import pytest

from data.user_data import UserData
from method_api.create_user import CreateUser


class TesteUser:

    @allure.title('Тест на регистрацию пользователь и проверок верификаций пользователя')
    @pytest.mark.parametrize('param', UserData.param)
    def test_create_user(self, param):
        data, code, key, message = param
        resalt_request = CreateUser.create_user_request(data)
        assert resalt_request.status_code == code and resalt_request.json()[key] == message