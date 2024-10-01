from faker import Faker

fake = Faker()


class Payloads:
    """Данные необходимые для эндпоинтов users"""

    def get_data_for_create_user(self):
        data = {
            "email": fake.email(),
            "password": fake.password(length=10),
            "name": fake.first_name(),
            "nickname": fake.user_name()
        }
        return data
