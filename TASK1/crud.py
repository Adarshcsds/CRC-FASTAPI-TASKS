from sqlmodel import Session, select

from models import Item, ItemStatus
from schemas import ItemCreate, ItemUpdate


def create_item(
    session: Session,
    item_data: ItemCreate
):

    item = Item(**item_data.model_dump())

    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def get_all_items(session: Session):

    statement = select(Item)

    return session.exec(statement).all()


def get_item(
    session: Session,
    item_id: int
):

    return session.get(Item, item_id)


def update_item(
    session: Session,
    item: Item,
    item_data: ItemUpdate
):

    data = item_data.model_dump()

    for key, value in data.items():
        setattr(item, key, value)

    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def delete_item(
    session: Session,
    item: Item
):

    session.delete(item)
    session.commit()


def get_items_by_status(
    session: Session,
    item_status: ItemStatus
):

    statement = select(Item).where(
        Item.status == item_status
    )

    return session.exec(statement).all()


def get_items_by_category(
    session: Session,
    category: str
):

    statement = select(Item).where(
        Item.category == category
    )

    return session.exec(statement).all()