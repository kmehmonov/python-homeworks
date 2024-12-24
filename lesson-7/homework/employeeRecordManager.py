import json

file_name = r"lesson-7\homework\employee.txt"

class Employee:
    """Create an employee"""

    def __init__(self, id: int, name: str, position: str, salary: float | int) -> "Employee":
        self.__id = id
        self.__name = name.capitalize()
        self.__position = position.capitalize()
        self.__salary = float(salary)

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self.__name = new_name.capitalize()

    def get_salary(self) -> float:
        return self.__salary

    def set_salary(self, new_salary: float | int) -> None:
        if not isinstance(new_salary, (float, int)):
            raise TypeError("Salary must be a float or int")
        self.__salary = float(new_salary)

    def get_position(self) -> str:
        return self.__position

    def set_position(self, new_position: str) -> None:
        if not isinstance(new_position, str):
            raise TypeError("Position must be a string")
        self.__position = new_position.capitalize()

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "name": self.__name,
            "position": self.__position,
            "salary": self.__salary,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Employee":
        return cls(
            id=data["id"],
            name=data["name"],
            position=data["position"],
            salary=data["salary"],
        )

    def __repr__(self):
        return f"Employee{self.to_dict()}"


class EmployeeManager:
    """Manage all employees"""

    def __init__(self):
        self.employee_database = dict()

    def add_employee(self, employee: Employee) -> None:
        if employee.get_id() in self.employee_database:
            print(f"Employee ID {employee.get_id()} already exists. Skipping addition.")
            return
        self.employee_database[employee.get_id()] = employee

    def view_all(self) -> None:
        if not self.employee_database:
            print("No employees to display.")
        try:
            keys = ["id", "name", "position", "salary"]
            sortby = int(input("Enter number for sorting: 1-id; 2-name; 3-position; 4-salary"))
            sorteddata = sorted(self.employee_database.values(), key=lambda emp: getattr(emp, f"get_{keys[sortby-1]}")())
            for employee in sorteddata:
                print(employee)
        except ValueError:
            print("Printed without sorting")  

    def search_employee(self, id: int) -> None:
        employee = self.employee_database.get(id)
        if employee:
            print(employee)
        else:
            print(f"Employee with ID {id} not found.")

    def update_employee(self, id: int, name=None, position=None, salary=None) -> None:
        employee = self.employee_database.get(id)
        if not employee:
            print(f"Employee with ID {id} not found.")
            return
        if name:
            employee.set_name(name)
        if position:
            employee.set_position(position)
        if salary:
            employee.set_salary(salary)
        print(f"Employee {id} updated successfully.")

    def delete_employee(self, id: int) -> None:
        if id in self.employee_database:
            del self.employee_database[id]
            print(f"Employee {id} deleted successfully.")
        else:
            print(f"Employee with ID {id} not found.")

    def load(self, file_name: str = file_name, format: str = "json") -> None:
        try:
            with open(file=file_name, mode="r") as file:
                if format == "json":
                    data = json.load(file)
                    self.employee_database = {
                        int(emp_id): Employee.from_dict(emp_data) for emp_id, emp_data in data.items()
                    }
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty database.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {file_name}. Starting with an empty database.")

    def write(self, file_name: str = file_name, format: str = "json") -> None:
        try:
            with open(file=file_name, mode="w") as file:
                if format == "json":
                    json.dump({emp.get_id(): emp.to_dict() for emp in self.employee_database.values()}, file, indent=4)
        except Exception as e:
            print(f"Error saving to file: {e}")


def print_menu():
    print("""
        1. Add new employee record
        2. View all employee records
        3. Search for an employee by Employee ID
        4. Update an employee's information
        5. Delete an employee record
        6. Save and Exit
    """)


def option_handling(option, employee_data: EmployeeManager):
    match option:
        case 1:
            try:
                while True:
                    id = int(input("Enter employee ID: "))
                    if id not in employee_data.employee_database:
                        break
                    else:
                        print("Enter unique ID. Try again!")
                name = input("Enter employee name: ")
                position = input("Enter employee position: ")
                salary = float(input("Enter employee salary: "))
                employee = Employee(id, name, position, salary)
                employee_data.add_employee(employee)
                print("New employee added successfully.")
            except ValueError:
                print("Invalid input. Please try again.")
        case 2:
            employee_data.view_all()
        case 3:
            try:
                id = int(input("Enter employee ID: "))
                employee_data.search_employee(id)
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
        case 4:
            try:
                id = int(input("Enter employee ID: "))
                name = input("Enter new name (leave blank to skip): ")
                position = input("Enter new position (leave blank to skip): ")
                salary_input = input("Enter new salary (leave blank to skip): ")
                salary = float(salary_input) if salary_input else None
                employee_data.update_employee(id, name or None, position or None, salary)
            except ValueError:
                print("Invalid input. Please try again.")
        case 5:
            try:
                id = int(input("Enter employee ID: "))
                employee_data.delete_employee(id)
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
        case 6:
            employee_data.write()
            print("Database saved. Exiting system.")
            return False
        case _:
            print("Invalid option, please try again.")
    return True

def main():
    print("=" * 40)
    print("Welcome to Employee Manager".center(40))
    print("=" * 40)

    employee_data = EmployeeManager()
    employee_data.load(file_name=file_name, format="json")

    while True:
        print_menu()
        try:
            option = int(input("Choose an option: "))
            if not option_handling(option, employee_data):
                break
        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
