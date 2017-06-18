[![CircleCI](https://circleci.com/gh/elinaldosoft/employee_manager.svg?style=svg)](https://circleci.com/gh/elinaldosoft/employee_manager)
[![Scrutinizer Coverage](https://img.shields.io/scrutinizer/coverage/g/filp/whoops.svg)]()

# Employee Manager

### Administration app Online:
- https://employee-manager-01.herokuapp.com/admin
- user: admin
- passwd: admin153


### RESTful API:

* List Employees (GET) (https://employee-manager-01.herokuapp.com/employee/)
```
curl -H "Content-Type: application/javascript" https://employee-manager-01.herokuapp.com/employee/
```
* Add Employees (POST) (https://employee-manager-01.herokuapp.com/employee/add)

```
curl -XPOST -H "Content-Type: application/json" https://employee-manager-01.herokuapp.com/employee/add -d '{"name": "Dr. Robert Bruce Banner", "email": "hulk@marvel.com", "departament": "Pesquisa"}'
```

* Delete Employees (DELETE) (https://employee-manager-01.herokuapp.com/employee/del)

```
curl -XDELETE -H "Content-Type: application/json" https://employee-manager-01.herokuapp.com/employee/del -d '{"email": "hulk@marvel.com"}'
```


### To running project

```
pip install -r requirements/dev-requirements.txt
python manage.py migrate
python manage.py createsuperuser <-- To create the user admin
```

### To running tests

```
coverage run manage.py test
```


#### Details Project
- Python 3.6
- Django 1.10.5
- CircleCI (Continuous Integration)