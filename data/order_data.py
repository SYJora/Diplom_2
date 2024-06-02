from method_api.order_user import OrderMethod


class DataOrder:

    ORDER = {
        "ingredients": OrderMethod.get_ingredients()
    }

    ORDER_EPTY = {
        "ingredients": []
    }

    ORDER_INCORRECT_HESH_NAME = {
        "ingredients": ['2565323', '2153412']
    }

    param = [
        (ORDER, 200, 'success', True),
        (ORDER_EPTY, 400, 'success', False),
        (ORDER_INCORRECT_HESH_NAME, 500, 'success', True)
    ]