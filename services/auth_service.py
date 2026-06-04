import allure
import requests

from config.settings import settings
from models.request.auth_request import AuthRequest
from models.response.auth_response import AuthResponse
from utils.attachments import attach_request, attach_response


class AuthService:

    @staticmethod
    @allure.step("Create auth token")
    def create_token() -> AuthResponse:
        url = f"{settings.base_url}/auth"

        payload = AuthRequest(
            username=settings.username,
            password=settings.password,
        )

        response = requests.post(
            url,
            json=payload.model_dump(),
            timeout=10,
        )

        attach_request("POST", url, payload.model_dump())
        attach_response(response)

        assert response.status_code == 200

        return AuthResponse.model_validate(response.json())

    @staticmethod
    @allure.step("Create auth token with custom credentials")
    def create_token_with_credentials(username, password):
        url = f"{settings.base_url}/auth"

        payload = AuthRequest(
            username=username,
            password=password,
        )

        response = requests.post(
            url,
            json=payload.model_dump(),
            timeout=10,
        )

        attach_request("POST", url, payload.model_dump())
        attach_response(response)

        return response