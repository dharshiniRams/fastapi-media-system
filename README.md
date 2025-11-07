##FastAPI Media Store System

A simple and clean FastAPI application for managing customers and media items (books, music, videos, etc.).
This project uses FastAPI, SQLAlchemy, and Pydantic to demonstrate a complete CRUD system.
Features

    Add, update, delete customers
    Add, get, update, delete media items
    View all customers
    View all media
    SQLAlchemy ORM with PostgreSQL
    Automatic schema validation with Pydantic

##Project Structure
```
media_system/

│── crud.py

│── database.py

│── main.py

│── models.py

│── schemas.py

│── requirements.txt
```

##Installation & Setup

1. Clone the Repository
```
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

3. Create a Virtual Environment
```
python3 -m venv myenv
source myenv/bin/activate
```

3. Install Dependencies

```
pip install -r requirements.txt
```

##Database Setup

You can update the connection string in database.py to use PostgreSQL/MySQL or use SQLite.

SQLite example (already configured):

```
SQLALCHEMY_DATABASE_URL = "sqlite:///./media.db"
```

##Run the FastAPI Server

```
uvicorn main:app --reload
```

The app will run at:
```
http://127.0.0.1:8000
```

Interactive API docs:
```
http://127.0.0.1:8000/docs
```
##API Endpoints

Customers

Method - Endpoint	      - Description

POST	 - /customer	    - Create customer
GET	   - /customers	Get - all customers
GET	   - /customer/{id}	- Get customer by ID
DELETE - /customer/{id}	- Delete customer

Media

Method	 - Endpoint	   - Description

POST	   - /media	     - Add media item
GET	     - /media	     - Get all media
GET	     - /media/{id} - Get media by ID
PUT	     - /media/{id} - Update media details
DELETE	 - /media/{id} - Delete media item
Testing

Use docs UI:
```
http://127.0.0.1:8000/docs
```
or use tools like:
```
    Postman

    Thunder Client

    cURL
```

This project is part of learning FastAPI and is free to use.

