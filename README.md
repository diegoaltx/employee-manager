# employee-manager

Django coding test.

* A Django Admin panel to manage employees' data
* An API to list, add and remove employees

## Installation

```
$ virtualenv -p python3 venv
$ source venv/bin/activate

$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py createsuperuser

$ python manage.py runserver
```

## Usage

### Django admin panel

Access http://localhost:8000/admin with superuser credentials. At admin panel you can:

* Add and change users.
* Add and refresh API Tokens.
* Add and change departments.
* Add and change employees.

### API

Before use API you will need to create an **Auth Token** on Admin Panel.

A complete **documentation of API endpoints** is available at http://localhost:8000/docs/ on your development server. There you also can test API calls and get code examples for Shell, Python and Javascript.

### API Examples

#### Create a department

Request:

```
curl -H "Authorization: Bearer YOUR-AUTH-TOKEN" -H "Content-type: application/json" -H "Accept: application/json" -X POST http://localhost:8000/departments -d '{"name": "Sales"}'
```

Response:

```
{"id": 1, "name": "Sales"}
```

#### Create an employee

Request:

```
curl -H "Authorization: Bearer YOUR-AUTH-TOKEN" -H "Content-type: application/json" -H "Accept: application/json" -X POST http://localhost:8000/employees -d '{"name": "Person One", "email": "person.one@company.com", "department_id": 1}'
```

Response:

```
{
  "id": 1,
  "name": "Person One",
  "email": "person.one@company.com",
  "department_id": 1,
  "department": {"id":1, "name": "Sales"},
  "date_created": "2017-04-03T01:49:03.347956Z",
  "date_modified": "2017-04-03T01:49:03.348025Z"
}
```

#### List employees

Request:

```
curl -H "Authorization: Bearer YOUR-AUTH-TOKEN" -H "Content-type: application/json" -H "Accept: application/json" -X GET http://localhost:8000/employees
```

Response:

```
[
  {
    "id": 1,
    "name": "Person One",
    "email": "person.one@company.com",
    "department_id": 1,
    "department": {"id": 1, "name": "Sales"},
    "date_created": "2017-04-03T01:47:35.681104Z",
    "date_modified": "2017-04-03T01:47:35.681236Z"
  },
  {
    "id": 2,
    "name": "Person Two",
    "email": "person.two@company.com",
    "department_id": 2,
    "department": {"id": 2,"name": "Marketing"},
    "date_created": "2017-04-03T01:49:03.347956Z",
    "date_modified": "2017-04-03T01:49:03.348025Z"
  }
]
```

#### Partial update an employee

Request:

```
curl -H "Authorization: Bearer YOUR-AUTH-TOKEN" -H "Content-type: application/json" -H "Accept: application/json" -X PATCH http://localhost:8000/employees/2 -d '{"name": "Person Updated"}'
```

Response:

```
{
  "id": 2,
  "name": "Person Updated",
  "email": "person.two@company.com",
  "department_id": 2,
  "department": {"id": 2,"name": "Marketing"},
  "date_created": "2017-04-03T01:49:03.347956Z",
  "date_modified": "2017-04-03T02:01:45.946391Z"
}
```

### Delete an employee

Request:

```
curl -H "Authorization: Bearer YOUR-AUTH-TOKEN" -H "Content-type: application/json" -H "Accept: application/json" -X DELETE http://localhost:8000/employees/13
```

Empty Response

### See more

A complete **documentation of API endpoints** is available at http://localhost:8000/docs/ on your development server. There you also can test API calls and get code examples for Shell, Python and Javascript.

## Testing

```
$ python manage.py test
```

## Requirements

* Python 3.4+
* Django 1.10
* Django Rest Framework 3.6
* Coreapi 2.3
