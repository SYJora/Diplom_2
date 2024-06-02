import requests

from data.login_data import DataLogin
from urls import Urls


class LoginUser:

    @staticmethod
    def log_in(data):
        return requests.post(Urls.BASE_URL + Urls.LOGIN_USER, json=data)

    @staticmethod
    def changest_user_data(token, data):
        return requests.patch(Urls.BASE_URL + Urls.CHANGEST_USER_DATA, headers = token, json = data)

    def test_create_user_log_out(self, data):
        respons = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=data)
        requests.post(Urls.BASE_URL + Urls.LOG_OUT, json={
            "token": respons.json()['refreshToken']})
        return respons


