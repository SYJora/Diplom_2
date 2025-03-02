import allure
import requests

from data.login_data import DataLogin
from urls import Urls


class LoginUser:

    @allure.step('Изменяют данные пользователя')
    def changest_user_data(self, token, data):
        return requests.patch(Urls.BASE_URL + Urls.CHANGEST_USER_DATA, headers = token, json = data)

    @allure.step('Создает пользователя возврошяет токин выхода')
    def test_create_user_log_out(self, data):
        respons = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=data)
        requests.post(Urls.BASE_URL + Urls.LOG_OUT, json={
            "token": respons.json()['refreshToken']})
        return respons


