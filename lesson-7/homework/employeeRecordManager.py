import json
file_name = "employee.txt"

class Employee:
    """Create an employee"""

    def __init__(self, id: int, name: str, position: str, salary: float | int) -> "Employee":
        self.__id = id
        self.__name = name
        self.__position = position
        self.__salary = float(salary)

    def __repr__(self):
        return f"Employee{self.__name, self.__position}"
    
    def get_id(self) -> int:
        return self.__id
    
    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("name must be string")
        self.__name = new_name
    
    def get_salary(self) -> float:
        return self.__salary

    def set_salary(self, new_salary: float | int) -> None:
        if not isinstance(new_salary, (float, int)):
            raise TypeError("Salary must be float")
        self.__salary = float(new_salary)

    def get_position(self) -> str:
        return self.__position

    def set_position(self, new_position: str) -> None:
        if not isinstance(new_position, str):
            raise TypeError("Postion must be string")
        self.__position = new_position
    
    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "name": self.__name,
            "position": self.__position,
            "salary": self.__salary
        }
    
    def from_dict():
        pass


class EmployeeManager:
    """Manage all employee"""

    def __init__(self):
        self.employee_database = dict()

    def add_employee(self, employee: Employee) -> None:
        self.employee_database[employee.get_id()] = employee

    def view_all(self) -> None:
        for employee in self.employee_database.values():
            print(employee)

    def search_employee(self, id: int) -> Employee:
        return self.employee_database[id]
    
    def update_employee(self, id: int, name=None, position=None, salary=None) -> None:
        employee = self.employee_database.get(id)
        if employee:
            if name:
                employee.set_name(name)
            if position:
                employee.set_position(position)
            if salary:
                employee.set_salary(salary)

    def delete_employee(self, id: int) -> None:
        del self.employee_database[id]

    def load(self, file_name, format):
        with open(file = file_name, mode="r") as file:
            if format == "json":
                self.employee_database = json.load(file)
            else:
                pass

    def write(self, file_name, format):
        with open(file = file_name, mode="w") as file:
            if format == "json":
                json.dump({emp.get_id(): emp.to_dict() for emp in self.employee_database.values()}, file, indent=4)
            else:
                pass

                        




emp = EmployeeManager()

employee1 = Employee(45236, "Kamoliddin", "O'qituvchi", 5)
employee2 = Employee(45237, "Jamshid", "O'qituvchi", 5)
emp.add_employee(employee1)
emp.add_employee(employee2)
emp.view_all()
emp.write(file_name, "json")




