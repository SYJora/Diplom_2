from base import Base


class UserData:

    user_maill = Base.generate_random_word(5)
    name = Base.generate_random_word(4)

    CREAT_USER = {
        "email": f"{user_maill}@mail.ru",
        "password": "12134",
        "name": name
    }

    COPY_USER = CREAT_USER

    CREAT_USER_WITHOUT_EMAIL = {
        "password": "12134",
        "name": name
    }

    CREAT_USER_WITHOUT_PASSWORD = {
        "email": f"{user_maill}@mail.ru",
        "name": name
    }

    CREAT_USER_WITHOUT_NAME = {
        "email": f"{user_maill}@mail.ru",
        "password": "12134"
    }


    param = [(CREAT_USER, 200, 'success', True),
             (COPY_USER, 403, 'message', 'User already exists'),
             (CREAT_USER_WITHOUT_EMAIL, 403, 'message', 'Email, password and name are required fields'),
             (CREAT_USER_WITHOUT_PASSWORD, 403, 'message', 'Email, password and name are required fields'),
             (CREAT_USER_WITHOUT_NAME, 403, 'message', 'Email, password and name are required fields')]

