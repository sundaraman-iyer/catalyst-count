# Catalyst Count - A Django Web Application

Catalyst Count is a Django-based web application that allows users to perform various tasks such as login, data upload, query building, and user management. The application is designed to use PostgreSQL as the database backend.

## Table of Contents
1. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
2. [Usage](#usage)
    - [Login](#login)
    - [Data Upload](#data-upload)
    - [Query Builder](#query-builder)
    - [Users](#users)

## Getting Started

### Prerequisites

Before running the application, make sure you have the following software installed:

- Python (version 3.11.x)
- Django (version 4.2.2)
- PostgreSQL (version 13.x)
- django-environ (version 0.10.0)
- djangorestframework (version 3.14.0)
- psycopg2-binary (version 2.9.6)

### Installation

1. Clone the repository OR Download the zip file & place it a suitable location. 

2. Navigate to the project folder.

        cd catalyst-count-main

3. Install all the project dependencies/pre-requisites.

        Ex.   pip install django

4. Set up the database.

        python manage.py makemigrations
        python manage.py migrate

5. Open .env file present inside catalyst_count folder. Ensure the SECRET_KEY and DATABASE_URL is present. The DATABASE_URL must be configured according to your       own PostgreSQL database. Format for updating DATABASE_URL:

        DATABASE_URL=postgres://your_db_user:your_db_password@localhost/your_db_name

    Replace your_db_user, your_db_password and your_db_name according to your own PostgreSQL database.

6. Create a superuser. Enter some dummy credentials to create superuser.

        python manage.py createsuperuser

## Usage

To run the development server, use the following command:

    python.exe .\manage.py runserver

The server will start running at http://localhost:8000/. Make sure there are no errors in the command prompt.

### Login
The login page can be accessed at http://localhost:8000/login. Users need to log in using the superuser credentials created during Installation to access other pages.

### Data Upload
The data upload page can be accessed at http://localhost:8000/dataupload. This page allows users to upload a large CSV file containing company data. 

### Query Builder
The query builder page can be accessed at http://localhost:8000/querybuilder. The query builder page allows users to apply filters on company data based on name, year founded, industry, and country. After applying the filters, clicking the "Query Data" button will display the count of records that match the filter criteria.

### Users
The users page can be accessed at http://localhost:8000/users. The users page displays a list of all users in the system. Only logged-in users can access this page.
