import allure
import requests

from config.settings import settings
from utils.attachments import attach_request, attach_response


class BookingService:

    @staticmethod
    @allure.step("Create booking")
    def create_booking(payload):
        url = f"{settings.base_url}/booking"

        response = requests.post(
            url,
            json=payload,
            timeout=10,
        )

        attach_request("POST", url, payload)
        attach_response(response)

        assert response.status_code == 200

        return response.json()

    @staticmethod
    @allure.step("Get booking")
    def get_booking(booking_id):
        url = f"{settings.base_url}/booking/{booking_id}"

        response = requests.get(
            url,
            timeout=10,
        )

        attach_request("GET", url)
        attach_response(response)

        assert response.status_code == 200

        return response.json()

    @staticmethod
    @allure.step("Update booking")
    def update_booking(booking_id, payload, token):
        url = f"{settings.base_url}/booking/{booking_id}"

        headers = {
            "Cookie": f"token={token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        response = requests.put(
            url,
            json=payload,
            headers=headers,
            timeout=10,
        )

        attach_request("PUT", url, payload, headers)
        attach_response(response)

        assert response.status_code == 200

        return response.json()

    @staticmethod
    @allure.step("Delete booking")
    def delete_booking(booking_id, token):
        url = f"{settings.base_url}/booking/{booking_id}"

        headers = {
            "Cookie": f"token={token}",
            "Content-Type": "application/json",
        }

        response = requests.delete(
            url,
            headers=headers,
            timeout=10,
        )

        attach_request("DELETE", url, headers=headers)
        attach_response(response)

        assert response.status_code == 201

        return response

    @staticmethod
    @allure.step("Get nonexistent booking")
    def get_nonexistent_booking(booking_id):
        url = f"{settings.base_url}/booking/{booking_id}"

        response = requests.get(
            url,
            timeout=10,
        )

        attach_request("GET", url)
        attach_response(response)

        return response

    @staticmethod
    @allure.step("Delete booking without token")
    def delete_booking_without_token(booking_id):
        url = f"{settings.base_url}/booking/{booking_id}"

        headers = {
            "Content-Type": "application/json",
        }

        response = requests.delete(
            url,
            headers=headers,
            timeout=10,
        )

        attach_request("DELETE", url, headers=headers)
        attach_response(response)

        return response