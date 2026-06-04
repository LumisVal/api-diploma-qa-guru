from pydantic import BaseModel


class BookingDatesResponse(BaseModel):
    checkin: str
    checkout: str


class BookingResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDatesResponse
    additionalneeds: str