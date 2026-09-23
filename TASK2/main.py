from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session

from TASK1.database import create_db_and_tables, get_session
from TASK1.models import Event, Reservation
from TASK1.schemas import EventCreate, EventUpdate, ReservationCreate
import crud


app = FastAPI(
    title="College Event Reservation API",
    description="API for managing college events and student reservations",
    version="1.0.0"
)


# --------------------------------
# DATABASE STARTUP
# --------------------------------

@app.on_event("startup")
def startup():

    create_db_and_tables()


# =================================
# EVENT APIs
# =================================


# 1. POST /events
@app.post(
    "/events",
    response_model=Event,
    status_code=status.HTTP_201_CREATED
)
def create_event(
    event_data: EventCreate,
    session: Session = Depends(get_session)
):

    return crud.create_event(
        session,
        event_data
    )


# 2. GET /events
@app.get(
    "/events",
    response_model=list[Event]
)
def get_events(
    session: Session = Depends(get_session)
):

    return crud.get_all_events(session)


# 3. GET /events/{event_id}
@app.get(
    "/events/{event_id}",
    response_model=Event
)
def get_event(
    event_id: int,
    session: Session = Depends(get_session)
):

    event = crud.get_event(
        session,
        event_id
    )

    if event is None:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event


# 4. PUT /events/{event_id}
@app.put(
    "/events/{event_id}",
    response_model=Event
)
def update_event(
    event_id: int,
    event_data: EventUpdate,
    session: Session = Depends(get_session)
):

    event = crud.get_event(
        session,
        event_id
    )

    if event is None:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return crud.update_event(
        session,
        event,
        event_data
    )


# 5. DELETE /events/{event_id}
@app.delete("/events/{event_id}")
def delete_event(
    event_id: int,
    session: Session = Depends(get_session)
):

    event = crud.get_event(
        session,
        event_id
    )

    if event is None:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    crud.delete_event(
        session,
        event
    )

    return {
        "message": "Event deleted successfully",
        "event_id": event_id
    }


# =================================
# RESERVATION APIs
# =================================


# 6. POST /events/{event_id}/reserve
@app.post(
    "/events/{event_id}/reserve",
    response_model=Reservation,
    status_code=status.HTTP_201_CREATED
)
def reserve_event(
    event_id: int,
    reservation_data: ReservationCreate,
    session: Session = Depends(get_session)
):

    # Check event exists
    event = crud.get_event(
        session,
        event_id
    )

    if event is None:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    result = crud.create_reservation(
        session,
        event,
        reservation_data
    )

    # Event is closed
    if result == "CLOSED":

        raise HTTPException(
            status_code=400,
            detail="Event is closed. Reservations are not allowed."
        )

    # Event is full
    if result == "FULL":

        raise HTTPException(
            status_code=400,
            detail="Event is full. No seats are available."
        )

    return result


# 7. GET /events/{event_id}/reservations
@app.get(
    "/events/{event_id}/reservations",
    response_model=list[Reservation]
)
def get_reservations(
    event_id: int,
    session: Session = Depends(get_session)
):

    event = crud.get_event(
        session,
        event_id
    )

    if event is None:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return crud.get_event_reservations(
        session,
        event_id
    )


# 8. DELETE /reservations/{reservation_id}
@app.delete(
    "/reservations/{reservation_id}"
)
def cancel_reservation(
    reservation_id: int,
    session: Session = Depends(get_session)
):

    reservation = crud.get_reservation(
        session,
        reservation_id
    )

    if reservation is None:

        raise HTTPException(
            status_code=404,
            detail="Reservation not found"
        )

    crud.delete_reservation(
        session,
        reservation
    )

    return {
        "message": "Reservation cancelled successfully",
        "reservation_id": reservation_id
    }


# 9. GET /events/{event_id}/availability
@app.get(
    "/events/{event_id}/availability"
)
def event_availability(
    event_id: int,
    session: Session = Depends(get_session)
):

    event = crud.get_event(
        session,
        event_id
    )

    if event is None:

        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return crud.get_availability(
        session,
        event
    )