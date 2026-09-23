from pydantic import EmailStr, field_validator
from sqlmodel import SQLModel

from TASK1.models import EventStatus


class EventCreate(SQLModel):

    title: str
    venue: str
    capacity: int
    organizer: str
    status: EventStatus

    @field_validator("title", "venue", "organizer")
    @classmethod
    def validate_text_fields(cls, value):

        if not value.strip():
            raise ValueError("This field must not be empty")

        return value

    @field_validator("capacity")
    @classmethod
    def validate_capacity(cls, value):

        if value <= 0:
            raise ValueError(
                "Capacity must be greater than 0"
            )

        return value


class EventUpdate(EventCreate):
    pass


class ReservationCreate(SQLModel):

    student_name: str
    roll_number: str
    email: EmailStr

    @field_validator("student_name", "roll_number")
    @classmethod
    def validate_fields(cls, value):

        if not value.strip():
            raise ValueError(
                "This field must not be empty"
            )

        return value