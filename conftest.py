import pytest
import requests

from data.login_data import DataLogin
from method_api.create_user import CreateUser
from method_api.login_user import LoginUser
from urls import Urls


@pytest.fixture(scope='function')
def create_log_in():
    CreateUser.create_user_request(DataLogin.CREAT_USER)
    respons = LoginUser.log_in(DataLogin.CREAT_USER)

@pytest.fixture(scope='function')
def creta_user():
    respons = CreateUser.create_user_request(DataLogin.CREAT_USER)
    tokken = respons.json()['accessToken']
    return tokken

@pytest.fixture(scope='session')
def test_create_user_log_out():
    respons = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=DataLogin.CREAT_USER)
    test = requests.post(Urls.BASE_URL + Urls.LOG_OUT, json={
        "token": respons.json()['refreshToken']})
    return respons

@pytest.fixture(scope='function')
def create_login_return_token():
    requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=DataLogin.CREAT_USER)
    respons = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, json=DataLogin.LOGIN_USER)
    return respons # Возьму токен от сюдава

@pytest.fixture(scope='function')
def create_user_log_in_log_out_return_token():
    requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=DataLogin.CREAT_USER)
    respons = requests.post(Urls.BASE_URL + Urls.LOGIN_USER, json=DataLogin.LOGIN_USER)
    requests.post(Urls.BASE_URL + Urls.LOG_OUT, json = {"token": respons.json()['refreshToken']})
    return respons # Возьму токен от сюдава




