import allure
import pytest
import requests

from data.user_data import UserData
from method_api.create_user import CreateUser
from urls import Urls


class TesteUser:

    @allure.title('Тест на регистрацию пользователь и проверок верификаций пользователя')
    @pytest.mark.parametrize('param', UserData.param)
    def test_create_user(self, param):
        data, code, key, message = param
        resalt_request = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json = data)
        assert resalt_request.status_code == code and resalt_request.json()[key] == message