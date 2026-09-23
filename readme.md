# FastAPI Application-Based Practical Assessment

This repository contains the complete implementation of the two tasks given in the FastAPI Application-Based Practical Assessment.

The projects demonstrate REST API development using FastAPI, database management using SQLite and SQLModel, request validation, CRUD operations, and API testing through Swagger UI.

---

## Technologies Used

- Python
- FastAPI
- SQLModel
- SQLite
- Pydantic
- Uvicorn
- Swagger UI

---

# Task 1 — Campus Lost & Found API

## 1. Project Description

The Campus Lost & Found API is a REST API developed using FastAPI for managing lost and found items on a college campus.

Students can report items that they have lost or found. The system stores information about each item, including its title, description, category, location, reporter, and current status.

The application uses SQLite as the database and SQLModel for database models and operations.

### Item Status

The following statuses are supported:

- Lost
- Found
- Returned

---

## 2. Technologies Used

- Python
- FastAPI
- SQLModel
- SQLite
- Pydantic
- Uvicorn
- Swagger UI

---

## 3. Installation Steps

Open a terminal inside the `TASK1` folder.

### Create a virtual environment

```bash
python -m venv venv
Activate the virtual environment

For Windows:

venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
4. Run the FastAPI Application

Run the following command inside the TASK1 folder:

uvicorn main:app --reload

The application will start at:

http://127.0.0.1:8000
5. Swagger UI

Open the following URL in your browser:

http://127.0.0.1:8000/docs

Swagger UI provides an interactive interface for testing all available API endpoints.

6. Available Endpoints
Method	Endpoint	Description
POST	/items	Create a new lost/found item
GET	/items	Get all reported items
GET	/items/{item_id}	Get a specific item
PUT	/items/{item_id}	Update an existing item
DELETE	/items/{item_id}	Delete an item
GET	/items/status/{item_status}	Filter items by status
GET	/items/category/{category}	Filter items by category

7. Validation and Error Handling

The API includes validation for:

Empty item titles are not allowed.
Descriptions must contain meaningful text.
Required fields must be provided.
Status can only be Lost, Found, or Returned.
A request for a non-existing item returns an appropriate HTTP error.
FastAPI validation errors are returned for invalid requests.

8. Database

Task 1 uses SQLite for persistent data storage.

The database engine is created using SQLModel's create_engine().

The database table is automatically created when the FastAPI application starts.

All item records are stored in the SQLite database rather than in a Python list or dictionary.

9. Application Logic
SQLite Database

The SQLite database engine is created using create_engine(). SQLModel metadata is used to automatically create the required database tables when the application starts.

SQLModel

SQLModel is used to define the Item database model and perform database operations such as creating, retrieving, updating, and deleting records.

Status and Category Filtering

Status filtering retrieves items matching the requested status.

Example:

GET /items/status/Lost

Category filtering retrieves items belonging to the requested category.

Example:

GET /items/category/Electronics
Non-Existing Item

When an item ID does not exist in the database, the API returns an appropriate HTTP 404 error.

Status Validation

The item status is defined using an enumeration containing:

Lost
Found
Returned

Therefore, invalid status values are rejected by FastAPI validation.

10. Proof of Work

Screenshots for Task 1 are available in:

TASK1/screenshots/

The screenshots demonstrate:

POST /items
GET /items
GET /items/{item_id}
PUT /items/{item_id}
DELETE /items/{item_id}
Status filtering
Category filtering
Invalid request and validation error
Task 2 — Campus Event Seat Reservation API
1. Project Description

The Campus Event Seat Reservation API is a REST API developed using FastAPI for managing college workshops, hackathons, seminars, and technical events.

Organizers can create and manage events, while students can reserve seats for available events.

The API checks whether an event exists, whether it is open, and whether seats are available before creating a reservation.

The application prevents overbooking and does not allow reservations for closed events.

SQLite is used for persistent storage and SQLModel is used for database models and operations.

Event Status

The following event statuses are supported:

Open
Closed
2. Technologies Used
Python
FastAPI
SQLModel
SQLite
Pydantic
Uvicorn
Email Validator
Swagger UI
3. Installation Steps

Open a terminal inside the TASK2 folder.

Create a virtual environment
python -m venv venv
Activate the virtual environment

For Windows:

venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
4. Run the FastAPI Application

Run the following command inside the TASK2 folder:

uvicorn main:app --reload

The application will start at:

http://127.0.0.1:8000
5. Swagger UI

Open the following URL in your browser:

http://127.0.0.1:8000/docs

Swagger UI provides an interactive interface for testing all available event and reservation endpoints.

6. Available Endpoints
Event Endpoints
Method	Endpoint	Description
POST	/events	Create a new event
GET	/events	Get all events
GET	/events/{event_id}	Get a specific event
PUT	/events/{event_id}	Update event information
DELETE	/events/{event_id}	Delete an event
Reservation Endpoints
Method	Endpoint	Description
POST	/events/{event_id}/reserve	Create a student reservation
GET	/events/{event_id}/reservations	Get all reservations for an event
DELETE	/reservations/{reservation_id}	Cancel a reservation
GET	/events/{event_id}/availability	Get event seat availability
7. Validation and Error Handling

The API includes validation for:

Event capacity must be greater than 0.
Student name must not be empty.
Roll number must be provided.
Email address must be valid.
A reservation must reference an existing event.
Reservations cannot be created for closed events.
Reservations cannot be created when an event is full.
8. Reservation Logic

Before creating a reservation, the API performs the following checks:

Checks whether the event exists.
Checks whether the event status is Open.
Retrieves the existing reservations for the event.
Counts the number of booked seats.
Compares booked seats with the event capacity.
Creates the reservation only if a seat is available.

This prevents the event from exceeding its defined capacity.

9. Seat Availability

The availability endpoint returns:

Total capacity
Number of booked seats
Number of remaining seats

Example:

{
    "capacity": 50,
    "booked": 32,
    "remaining": 18
}

The remaining seats are calculated using:

remaining = capacity - booked
10. Closed Event Handling

If an event is marked as:

Closed

new reservations are rejected.

This ensures that students cannot register for an event that is no longer accepting reservations.

11. Database

Task 2 uses SQLite for persistent data storage.

The database engine is created using SQLModel's create_engine().

The required database tables are automatically created when the FastAPI application starts.

SQLModel Session is used to perform database operations such as:

Creating events
Retrieving events
Updating events
Deleting events
Creating reservations
Retrieving reservations
Cancelling reservations
12. Application Logic
Event Existence Check

Before creating a reservation, the API checks whether the requested event exists.

If the event does not exist, an appropriate HTTP 404 error is returned.

Booked and Remaining Seats

The number of existing reservations is counted for the selected event.

The remaining seats are calculated as:

remaining = capacity - booked
Overbooking Prevention

A reservation is rejected when:

booked >= capacity

This prevents the number of reservations from exceeding the event capacity.

Closed Event Prevention

A reservation is rejected when the event status is:

Closed
SQLModel Session

SQLModel's Session is used to communicate with the SQLite database.

Database operations use methods such as:

session.get()
session.add()
session.commit()
session.refresh()
session.delete()
session.exec()
13. Proof of Work

Screenshots for Task 2 are available in:

TASK2/screenshots/

The screenshots demonstrate:

POST /events
GET /events
Successful reservation creation
GET event reservations
Event availability
Successful reservation cancellation
Unsuccessful reservation when the event is full or closed
Repository Structure
CRC-FASTAPI-TASKS/
│
├── README.md
├── .gitignore
│
├── TASK1/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── requirements.txt
│   └── screenshots/
│
└── TASK2/
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── crud.py
    ├── requirements.txt
    └── screenshots/
Testing

Both applications can be tested using Swagger UI.

Task 1
http://127.0.0.1:8000/docs
Task 2
http://127.0.0.1:8000/docs

The screenshots included in each task's screenshots folder provide proof of successful API execution and validation/error handling.

Challenges Faced / Additional Comments

A major challenge was implementing the event reservation capacity logic correctly.

The API had to ensure that reservations could not exceed the event's defined capacity and that reservations were rejected when an event was closed.

This was solved by checking the event status and counting existing reservations before creating a new reservation.

Input validation was also implemented for fields such as event capacity, student information, and email addresses.

Author

Adarsh Sushil Dubey

B.Tech — Computer Science & Data Science


