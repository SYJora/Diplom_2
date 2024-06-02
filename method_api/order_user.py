import requests

from urls import Urls


class OrderMethod:
    @staticmethod
    def get_ingredients():
        respons = requests.get(Urls.BASE_URL + Urls.LIST_INGR)
        ingr = []
        for i in range(3):
            ingr.append(respons.json()['data'][i]['_id'])
        return ingr

