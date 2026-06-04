import allure

from services.auth_service import AuthService


@allure.feature("Authorization")
@allure.title("Create auth token")
def test_create_auth_token():
    auth_response = AuthService.create_token()

    assert auth_response.token