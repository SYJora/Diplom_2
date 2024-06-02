import allure
import pytest
import requests

from data.login_data import DataLogin
from urls import Urls


@pytest.fixture(scope='function')
def create_log_in():
    requests.post(Urls.BASE_URL + Urls.CREATE_USER, json = DataLogin.CREAT_USER)

@pytest.fixture(scope='function')
def creta_user():
    respons = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json = DataLogin.CREAT_USER)
    return respons

@allure.step('Выход из системы')
@pytest.fixture(scope='session')
def test_create_user_log_out():
    respons = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=DataLogin.CREAT_USER)

@allure.step('Создание пользователя вход в систему возврат токина подключения')
@pytest.fixture(scope='function')
def create_login_return_token():
    requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=DataLogin.CREAT_USER)
    respons = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, json=DataLogin.LOGIN_USER)
    return respons # Возьму токен от сюдава

@allure.step('Создание пользователя вход и выход из системы')
@pytest.fixture(scope='function')
def create_user_log_in_log_out_return_token():
    requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=DataLogin.CREAT_USER)
    respons = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, json=DataLogin.LOGIN_USER)
    requests.post(Urls.BASE_URL + Urls.LOG_OUT, json = {"token": respons.json()['refreshToken']})
    return respons # Возьму токен от сюдава




