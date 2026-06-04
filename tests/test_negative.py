import allure

from services.auth_service import AuthService
from services.booking_service import BookingService
from utils.generators import generate_booking


@allure.feature("Authorization")
@allure.title("Unsuccessful authorization with invalid password")
def test_unsuccessful_authorization_with_invalid_password():
    response = AuthService.create_token_with_credentials(
        username="admin",
        password="wrong_password",
    )

    assert response.status_code == 200
    assert response.json()["reason"] == "Bad credentials"


@allure.feature("Booking")
@allure.title("Get nonexistent booking")
def test_get_nonexistent_booking():
    response = BookingService.get_nonexistent_booking(
        booking_id=999999999,
    )

    assert response.status_code == 404


@allure.feature("Booking")
@allure.title("Delete booking without token")
def test_delete_booking_without_token():
    payload = generate_booking()
    created_booking = BookingService.create_booking(payload)
    booking_id = created_booking["bookingid"]

    response = BookingService.delete_booking_without_token(
        booking_id,
    )

    assert response.status_code == 403