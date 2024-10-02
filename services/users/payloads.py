from faker import Faker

fake = Faker()


class Payloads:
    """Данные необходимые для эндпоинтов users"""

    session_data_for_user = data = {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.first_name(),
        "nickname": fake.user_name()
    }

    def get_data_for_user(self):
        data = {
            "email": fake.email(),
            "password": fake.password(length=10),
            "name": fake.first_name(),
            "nickname": fake.user_name()
        }
        return data
