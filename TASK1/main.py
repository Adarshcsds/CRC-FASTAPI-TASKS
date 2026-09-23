from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session

from database import create_db_and_tables, get_session
from models import Item, ItemStatus
from schemas import ItemCreate, ItemUpdate
import crud


app = FastAPI(
    title="College Lost & Found API",
    description="API for managing lost and found items on campus",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    create_db_and_tables()


@app.post(
    "/items",
    response_model=Item,
    status_code=status.HTTP_201_CREATED
)
def create_item(
    item_data: ItemCreate,
    session: Session = Depends(get_session)
):

    return crud.create_item(
        session,
        item_data
    )


# --------------------------------
# 2. GET ALL ITEMS
# GET /items
# --------------------------------

@app.get(
    "/items",
    response_model=list[Item]
)
def get_all_items(
    session: Session = Depends(get_session)
):

    return crud.get_all_items(session)


# --------------------------------
# 3. GET ITEM BY ID
# GET /items/{item_id}
# --------------------------------

@app.get(
    "/items/{item_id}",
    response_model=Item
)
def get_item(
    item_id: int,
    session: Session = Depends(get_session)
):

    item = crud.get_item(
        session,
        item_id
    )

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    return item


# --------------------------------
# 4. UPDATE ITEM
# PUT /items/{item_id}
# --------------------------------

@app.put(
    "/items/{item_id}",
    response_model=Item
)
def update_item(
    item_id: int,
    item_data: ItemUpdate,
    session: Session = Depends(get_session)
):

    item = crud.get_item(
        session,
        item_id
    )

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    return crud.update_item(
        session,
        item,
        item_data
    )


# --------------------------------
# 5. DELETE ITEM
# DELETE /items/{item_id}
# --------------------------------

@app.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    session: Session = Depends(get_session)
):

    item = crud.get_item(
        session,
        item_id
    )

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    crud.delete_item(
        session,
        item
    )

    return {
        "message": "Item deleted successfully",
        "item_id": item_id
    }


# --------------------------------
# 6. GET ITEMS BY STATUS
# GET /items/status/{status}
# --------------------------------

@app.get(
    "/items/status/{item_status}",
    response_model=list[Item]
)
def get_items_by_status(
    item_status: ItemStatus,
    session: Session = Depends(get_session)
):

    return crud.get_items_by_status(
        session,
        item_status
    )


# --------------------------------
# 7. GET ITEMS BY CATEGORY
# GET /items/category/{category}
# --------------------------------

@app.get(
    "/items/category/{category}",
    response_model=list[Item]
)
def get_items_by_category(
    category: str,
    session: Session = Depends(get_session)
):

    return crud.get_items_by_category(
        session,
        category
    )