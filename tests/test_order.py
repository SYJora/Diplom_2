import allure
import pytest
import requests

from data.order_data import DataOrder
from urls import Urls


class TestOrder:

    @allure.title('Создание заказа авторизированным пользователем')
    @pytest.mark.parametrize('param', DataOrder.param)
    def test_sing_in_user_make_order(self, create_login_return_token, param):
        data, cod, masseg, result = param
        respons = requests.post(Urls.BASE_URL + Urls.CREATE_ORDER,
                      headers={"Authorization": create_login_return_token.json()['accessToken']}, json=data)
        assert respons.status_code == cod and respons.json()[masseg] == result

    @allure.title('Создание заказа не авторизированным пользователем')
    def test_log_out_user_get_order(self,create_user_log_in_log_out_return_token):
        respons = requests.post(Urls.BASE_URL + Urls.CREATE_ORDER,
                                json=DataOrder.ORDER)
        assert respons.status_code == 400 and respons.json()['message'] == "Ingredient ids must be provided"

    @allure.title('Получение заказа конкретного пользователя')
    def test_get_order_current_user(self, create_login_return_token):
        order = requests.post(Urls.BASE_URL + Urls.CREATE_ORDER,
                      headers={"Authorization": create_login_return_token.json()['accessToken']},
                      json = DataOrder.ORDER)
        respons = requests.get(Urls.BASE_URL + Urls.CREATE_ORDER,
                     headers={"Authorization": create_login_return_token.json()['accessToken']})
        assert order.json()['name'] == respons.json()['orders'][0]['name']

    @allure.title('Получение заказа конкретного пользователя, который не авторизирован')
    def test_get_order_not_login_user(self, create_login_return_token):
        requests.post(Urls.BASE_URL + Urls.CREATE_ORDER,
                              headers={"Authorization": create_login_return_token.json()['accessToken']},
                              json=DataOrder.ORDER)
        respons = requests.get(Urls.BASE_URL + Urls.CREATE_ORDER)
        assert respons.status_code == 401 and respons.json()['message'] == "You should be authorised"
