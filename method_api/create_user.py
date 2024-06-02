import requests
from urls import Urls


class CreateUser:

     @staticmethod
     def create_user_request(data):
         return requests.post(Urls.BASE_URL + Urls.CREATE_USER, json = data)
