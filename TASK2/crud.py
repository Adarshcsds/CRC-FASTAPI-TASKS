from sqlmodel import Session, select, func

from TASK1.models import Event, Reservation, EventStatus
from TASK1.schemas import EventCreate, EventUpdate, ReservationCreate


# --------------------------------
# EVENT CRUD
# --------------------------------

def create_event(
    session: Session,
    event_data: EventCreate
):

    event = Event(**event_data.model_dump())

    session.add(event)
    session.commit()
    session.refresh(event)

    return event


def get_all_events(session: Session):

    statement = select(Event)

    return session.exec(statement).all()


def get_event(
    session: Session,
    event_id: int
):

    return session.get(Event, event_id)


def update_event(
    session: Session,
    event: Event,
    event_data: EventUpdate
):

    data = event_data.model_dump()

    for key, value in data.items():
        setattr(event, key, value)

    session.add(event)
    session.commit()
    session.refresh(event)

    return event


def delete_event(
    session: Session,
    event: Event
):

    session.delete(event)
    session.commit()


# --------------------------------
# RESERVATION LOGIC
# --------------------------------

def create_reservation(
    session: Session,
    event: Event,
    reservation_data: ReservationCreate
):

    statement = select(Reservation).where(
        Reservation.event_id == event.id
    )

    reservations = session.exec(statement).all()

    booked = len(reservations)

    if event.status == EventStatus.Closed:
        return "CLOSED"

    if booked >= event.capacity:
        return "FULL"

    reservation = Reservation(
        event_id=event.id,
        **reservation_data.model_dump()
    )

    session.add(reservation)
    session.commit()
    session.refresh(reservation)

    return reservation


def get_event_reservations(
    session: Session,
    event_id: int
):

    statement = select(Reservation).where(
        Reservation.event_id == event_id
    )

    return session.exec(statement).all()


def get_reservation(
    session: Session,
    reservation_id: int
):

    return session.get(
        Reservation,
        reservation_id
    )


def delete_reservation(
    session: Session,
    reservation: Reservation
):

    session.delete(reservation)
    session.commit()


# --------------------------------
# AVAILABILITY
# --------------------------------

def get_availability(
    session: Session,
    event: Event
):

    statement = select(Reservation).where(
        Reservation.event_id == event.id
    )

    reservations = session.exec(statement).all()

    booked = len(reservations)

    remaining = event.capacity - booked

    return {
        "capacity": event.capacity,
        "booked": booked,
        "remaining": remaining
    }