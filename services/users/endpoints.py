import os

HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" \
    else "https://release-gs.qa-playground.com/api/v1"


class Endpoints:
    """Эндпоинты относящиеся к users"""
    create_user = f"{HOST}/users"
    get_user_by_id = lambda self, uuid: f"{HOST}/users/{uuid}"
    login_user = f"{HOST}/users/login"
    get_users = f"{HOST}/users"
    delete_user = lambda self, uuid: f"{HOST}/users/{uuid}"
