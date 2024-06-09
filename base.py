import string
import random

import allure

from method_api.create_user import CreateUser


class Base:

    @allure.step('Генерация данных для тела запроса')
    def generate_random_word(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def create_log_in_user(self, data_creat, data_login):
        CreateUser.create_user_request(data_creat)
        respons_log = CreateUser.log_in(data_login)
        token = respons_log.json()['refreshToken']
        return token


