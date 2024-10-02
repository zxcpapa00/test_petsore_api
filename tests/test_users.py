import allure
import pytest

from config.base_test import BaseTest


@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_id(user.uuid)

    @allure.title("Get all users")
    def test_get_all_users(self):
        self.api_users.get_all_users()

    @allure.title("Login user")
    def test_login_user(self):
        email, password, _ = self.api_users.create_user_for_login()
        self.api_users.login_user(email, password)

    @allure.title("Delete user")
    def test_delete_user(self):
        user = self.api_users.create_user()
        self.api_users.delete_user(user.uuid)
        self.api_users.get_deleted_user(user.uuid)

    @allure.title("Update user")
    def test_update_user(self):
        user_create = self.api_users.create_user()
        user_update = self.api_users.update_user_data(user_create.uuid)
        assert user_update.uuid == user_create.uuid
        assert user_update != user_create

    @allure.title("Login deleted user")
    @pytest.mark.negative_cases
    def test_login_deleted_user(self):
        email, password, user_uuid = self.api_users.create_user_for_login()
        self.api_users.login_user(email, password)
        self.api_users.delete_user(user_uuid)
        self.api_users.login_non_existent_user(email, password)

    @allure.title("Login user with random data")
    @pytest.mark.negative_cases
    def test_login_user_with_random_data(self):
        self.api_users.login_user_with_random_data()

    @allure.title("Create existing user")
    @pytest.mark.negative_cases
    def test_create_existing_user(self):
        self.api_users.create_static_user()
        self.api_users.create_existing_user()
