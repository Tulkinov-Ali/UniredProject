# UniredProject

This project provides endpoints for managing currency exchange rates and performing currency conversions. It utilizes
Django REST Framework for building the API.

# Installation

1. Clone the repository:

```
git clone https://github.com/Tulkinov-Ali/UniredProject.git
cd UniredProject
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```

4. Start the server

```
python manage.py runserver
```

The API will be accessible at http://localhost:8000/.

# Currency Exchange Rate Fetching Task

- **Save Currency Rate**

    This Celery task is designed to fetch currency exchange rates from an external API and save them into the database. It
    utilizes Django ORM for database operations and Celery for asynchronous task execution.

# Setup
1. Installation: Ensure you have the necessary Python packages installed. 
   ```
   pip install celery
   ```
2. Install a Broker using Docker
    ```
    docker run -d -p 6379:6379 redis
    ```
3. Install Celery Beat
   ```
   pip install django-celery-beat
   ```
4. Install Celery Results
   ```
   pip install django-celery-results
   ```
5. ```python manage.py migrate``` after installing packages above
6. **Starting the Celery worker**
    ```
    celery -A yourprojectname worker -l INFO
    ```
   **Note:**
   `if you are Windows user start celery worker using code below`
    ```
    celery -A yourprojectname worker -l INFO eventlet
    ```
7. **Starting the Celery beat for scheduling**
    ```
    celery -A yourprojectname beat -l INFO
    ```
- **Currency Conversion**

  Endpoint to convert an amount from Uzbekistan Som (UZS) to the specified currency.

    - **URL:** `/api/v1/currencies/`
    - **Method:** `POST`
    - **Request Body:**
        - `uzs_amount`: The amount in Uzbekistan Som (UZS) to be converted.
        - `currency_code`: The code of the currency to which the conversion should be made.
    - **Response:**
        - `Success`: HTTP 200 OK with converted amount and currency name.
        - `Error`: HTTP 400 BAD REQUEST with error message if currency code or amount is not provided, or if exchange
          rate not found
          for the specified currency code.

- **Retrieve All Currencies**
  Endpoint to retrieve a list of all currencies from the database with optional filtering.
    - **URL:** `/api/v1/currencies/`
    - **Method:** `GET`
    - **Query Parameters:**
        - `date`: Filter currencies by date (year, month, day, exact).
        - `code`: Filter currencies by code (exact).
        - `ccy`: Filter currencies by currency ISO code (exact).
    - **Response:**
        - **Success:** HTTP 200 OK with a list of currencies.
- **Chart**

    to visualize currency rate
    - **URL:** `/api/v1/rate-chart/`
- **Redoc**
    Swagger documentation
    - **URL:** `/api/v1/redoc/`
    

# Dependencies

- **Django**
- **Celery**
- **Django REST Framework**
- **Requests**