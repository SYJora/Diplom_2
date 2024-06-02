import allure
import requests
from urls import Urls


class CreateUser:

     @allure.step("Создание нового пользователя")
     @staticmethod
     def create_user_request(data):
         return requests.post(Urls.BASE_URL + Urls.CREATE_USER, json = data)
