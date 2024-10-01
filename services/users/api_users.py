import allure
import requests

from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from utils.helper import Helper
from config.headers import Headers
from services.users.models.user_model import UserModel, UsersModel


class UsersAPI(Helper):
    """Тесты users"""

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create user")
    def create_user(self):
        """Регистрация пользователя"""
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.get_data_for_user()
        )
        assert response.status_code == 200
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Create user for login")
    def create_user_for_login(self):
        """Регистрация пользователя для авторизации"""
        data = self.payloads.get_data_for_user()
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=data
        )
        assert response.status_code == 200
        return data.get("email"), data.get("password")

    @allure.step("Get user by id")
    def get_user_by_id(self, uuid):
        """Получить пользователя по uuid"""
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic,
        )
        assert response.status_code == 200
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Get all users")
    def get_all_users(self):
        """Получение всех пользователей"""
        response = requests.get(
            url=self.endpoints.get_users,
            headers=self.headers.basic
        )
        self.attach_response(response.json())
        model = UsersModel(**response.json())
        return model

    @allure.step("Login user")
    def login_user(self, email, password):
        """Авторизация пользователя"""
        response = requests.post(
            url=self.endpoints.login_user,
            headers=self.headers.basic,
            json={"email": email, "password": password}
        )
        assert response.status_code == 200
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Delete user by id")
    def delete_user(self, uuid):
        """Удаление пользователя по uuid"""
        response = requests.delete(
            url=self.endpoints.delete_user(uuid),
            headers=self.headers.basic
        )
        assert response.status_code == 204

    @allure.step("Get deleted user by id")
    def get_deleted_user(self, uuid):
        """Получение удалённого пользователя"""
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic,
        )
        assert response.status_code == 404
        self.attach_response(response.json())

    @allure.step("Update user")
    def update_user_data(self, uuid):
        """Получение данных пользователя"""
        response = requests.patch(
            url=self.endpoints.update_user(uuid),
            headers=self.headers.basic,
            json=self.payloads.get_data_for_user()
        )
        assert response.status_code == 200
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model
