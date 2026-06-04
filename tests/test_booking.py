import allure
import requests

from config.settings import settings
from services.auth_service import AuthService
from services.booking_service import BookingService
from utils.generators import generate_booking


@allure.feature("Booking")
@allure.title("Create booking")
def test_create_booking():
    payload = generate_booking()

    booking = BookingService.create_booking(payload)

    assert booking["bookingid"] > 0


@allure.feature("Booking")
@allure.title("Get booking")
def test_get_booking():
    payload = generate_booking()

    booking = BookingService.create_booking(payload)

    booking_id = booking["bookingid"]

    actual_booking = BookingService.get_booking(
        booking_id
    )

    assert actual_booking["firstname"] == payload["firstname"]


@allure.feature("Booking")
@allure.title("Update booking")
def test_update_booking():
    token = AuthService.create_token().token

    payload = generate_booking()
    created_booking = BookingService.create_booking(payload)
    booking_id = created_booking["bookingid"]

    updated_payload = generate_booking()

    updated_booking = BookingService.update_booking(
        booking_id,
        updated_payload,
        token,
    )

    assert updated_booking["firstname"] == updated_payload["firstname"]
    assert updated_booking["lastname"] == updated_payload["lastname"]


@allure.feature("Booking")
@allure.title("Delete booking")
def test_delete_booking():
    token = AuthService.create_token().token

    payload = generate_booking()
    created_booking = BookingService.create_booking(payload)
    booking_id = created_booking["bookingid"]

    BookingService.delete_booking(
        booking_id,
        token,
    )

    response = requests.get(
        f"{settings.base_url}/booking/{booking_id}",
        timeout=10,
    )

    assert response.status_code == 404