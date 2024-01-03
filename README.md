# Assignment

It provides RESTful API endpoints for managing items.

## Prerequisites

- [Python](https://www.python.org/downloads/) (>=3.6)
- [Django](https://www.djangoproject.com/download/) (>=3.x)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Pipenv](https://pypi.org/project/pipenv/)


## Set Up

1. Clone the project.
2. Navigate to the project directory and open the terminal. And run the following command

   `pipenv shell` to create a virtual environment.

   `pipenv install` to install required dependencies.
3. Run the server using the following command to check if everything is working fine.

   `python manage.py runserver`
4. Terminate the server and run the following command to apply the migrations.

    `python manage.py migrate`
5. Create a super user using the following command.

    `python manage.py createsuperuser`
6. Run the server using the following command.

    `python manage.py runserver` The API will be available at http://127.0.0.1:8000/.


## API Endpoints

### Item
&emsp; Create Item: POST /item/create/

&emsp; Get Item: GET /item/1/

&emsp; List Items: GET /item/

&emsp; Update Item: PUT/PATCH /item/1/

&emsp; Delete Items: DELETE /item/1/
