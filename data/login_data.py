from base import Base

class DataLogin:

    user_maill = Base.generate_random_word(5)
    name = Base.generate_random_word(4)

    CREAT_USER = {
        "email": f"{user_maill}@mail.ru",
        "password": "12134",
        "name": name
    }

    LOGIN_USER = {
        "email": f"{user_maill}@mail.ru",
        "password": "12134"
    }

    INCORRECT_LOGIN_USER = {
        "email": "wreewyyw@mail.ru",
        "password": "12134"
    }

    CHANGEST_USER_EMAIL = {
        "email": f"{user_maill}try@mail.ru"
    }

    CHANGEST_USER_PASSWORD = {
        "password": "12134"
    }

    CHANGEST_USER_NAME = {
        "name": "test_c"
    }

    TOKKEN = {
        "authorization": str
    }

    param = [(LOGIN_USER, 200, 'success', True),
             (INCORRECT_LOGIN_USER, 401, 'message', 'email or password are incorrect')]

    param_data_changest = [
        (CHANGEST_USER_EMAIL, 401, 'success', False),
        (CHANGEST_USER_PASSWORD, 401, 'success', False),
        (CHANGEST_USER_NAME, 401, 'success', False)
    ]
