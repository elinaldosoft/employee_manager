[![CircleCI](https://circleci.com/gh/elinaldosoft/employee_manager.svg?style=svg)](https://circleci.com/gh/elinaldosoft/employee_manager)
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
curl -H "Content-Type: application/json" https://employee-manager-01.herokuapp.com/employee/ -d '{"name": "Dr. Robert Bruce Banner", "email": "Dr. Robert Bruce Banner"}'
```

* Delete Employees (DELETE) (https://employee-manager-01.herokuapp.com/employee/del)
