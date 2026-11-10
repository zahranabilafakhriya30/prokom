from employee import Employee

def test_give_default_raise():
    employee = Employee("Zahra", "Nabila", 5000000)
    employee.give_raise()

    assert employee.salary == 5005000

def test_give_custom_raise():
    employee = Employee("Zahra", "Nabila", 5000000)
    employee.give_raise(1000000)

    assert employee.salary == 6000000