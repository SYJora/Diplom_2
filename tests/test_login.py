import pytest
import requests

from data.login_data import DataLogin
from method_api.login_user import LoginUser
from urls import Urls


class TestLogin:

    @pytest.mark.parametrize('param', DataLogin.param)
    def test_log_in(self, create_log_in, param):
        data, code, key, message = param
        respons = LoginUser.log_in(data)
        assert respons.status_code == code and respons.json()[key] == message

    def test_changest_log_in_user_data(self, creta_user):
        respons = LoginUser.changest_user_data(token= {'Authorization': creta_user}, data=DataLogin.CHANGEST_USER_DATA)
        assert respons.json()['success'] == True and respons.json()['user']['name'] == DataLogin.CHANGEST_USER_DATA['name']

    @pytest.mark.parametrize('param_data_changest', DataLogin.param_data_changest)
    def test_make_changest_not_login_user(self, param_data_changest, test_create_user_log_out):
        data, cod, mes, res = param_data_changest
        request = requests.patch(Urls.BASE_URL + Urls.CHANGEST_USER_DATA,
                       headers={'Authorization': test_create_user_log_out.json()['accessToken']}, json=data)
        assert request.status_code == cod and request.json()[mes] == res



