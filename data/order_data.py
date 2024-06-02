from method_api.order_user import OrderMethod


class DataOrder:

    ORDER = {
        "ingredients": OrderMethod.get_ingredients()
    }

    ORDER_EPTY = {
        "ingredients": []
    }

    ORDER_INCORRECT_HESH_NAME = {
        "ingredients": 'kddk'
    }

    param = [
        (ORDER, 200, 'success', True),
        (ORDER_EPTY, 400, 'success', False),
    ]