from faker import Faker

fake = Faker()


class Payloads:
    """Данные необходимые для эндпоинтов users"""
    create_user = {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.first_name(),
        "nickname": fake.user_name()
    }
