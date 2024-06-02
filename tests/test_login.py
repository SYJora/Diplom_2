import allure
import pytest
import requests

from data.login_data import DataLogin
from urls import Urls


class TestLogin:

    @allure.title('Проверка входа пользователя в систему')
    @pytest.mark.parametrize('param', DataLogin.param)
    def test_log_in(self, create_log_in, param):
        data, code, key, message = param
        respons = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, json=data)
        assert respons.status_code == code and respons.json()[key] == message

    @allure.title('Проверка изменения данных авторизированного пользователя')
    def test_changest_log_in_user_data(self, creta_user):
        respons =requests.patch(Urls.BASE_URL + Urls.CHANGEST_USER_DATA,
                       headers= {"Authorization": creta_user.json()['accessToken']}, json=DataLogin.CHANGEST_USER_NAME)
        assert respons.json()['success'] == True and respons.json()['user']['name'] == DataLogin.CHANGEST_USER_NAME['name']

    @allure.title('Проверка изменения данных  не авторизированного пользователя')
    @pytest.mark.parametrize('param_data_changest', DataLogin.param_data_changest)
    def test_make_changest_not_login_user(self, param_data_changest, test_create_user_log_out):
        data, cod, mes, res = param_data_changest
        request = requests.patch(Urls.BASE_URL + Urls.CHANGEST_USER_DATA, json=data)
        assert request.status_code == cod and request.json()[mes] == res



