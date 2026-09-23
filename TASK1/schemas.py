from pydantic import field_validator
from sqlmodel import SQLModel

from models import ItemStatus


class ItemCreate(SQLModel):

    title: str
    description: str
    category: str
    location: str
    reported_by: str
    status: ItemStatus

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError("Title must not be empty")

        return value

    @field_validator("description")
    @classmethod
    def validate_description(cls, value):
        if len(value.strip()) < 5:
            raise ValueError(
                "Description must contain meaningful text"
            )

        return value

    @field_validator("category", "location", "reported_by")
    @classmethod
    def validate_required_fields(cls, value):

        if not value.strip():
            raise ValueError("This field is required")

        return value


class ItemUpdate(ItemCreate):
    pass