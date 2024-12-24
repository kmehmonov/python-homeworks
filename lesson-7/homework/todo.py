import json

file_name = r"lesson-7/homework/tasks.txt"

class Task:
    """
    Create a task.
    """

    def __init__(self, id: int, title: str, description: str, due_date, status: str) -> "Task":
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
        }


class TaskManager:
    """
    Manage all tasks.
    """

    def __init__(self) -> None:
        self.all_tasks = {}

    def add_task(self, task: Task) -> None:
        self.all_tasks[str(task.id)] = task.to_dict()

    def update_task(self, id: int, title: str = None, description: str = None, due_date=None, status: str = None) -> None:
        if str(id) not in self.all_tasks:
            print(f"Task with ID {id} not found.")
            return
        if title:
            self.all_tasks[str(id)]["title"] = title
        if description:
            self.all_tasks[str(id)]["description"] = description
        if due_date:
            self.all_tasks[str(id)]["due_date"] = due_date
        if status:
            self.all_tasks[str(id)]["status"] = status

    def delete_task(self, id: int) -> None:
        if str(id) in self.all_tasks:
            del self.all_tasks[str(id)]
        else:
            print(f"Task with ID {id} not found.")

    def view(self, filterby: str = None) -> None:
        if filterby:
            tasks = filter(lambda x: x["status"] == filterby, self.all_tasks.values())
        else:
            tasks = self.all_tasks.values()
        for task in tasks:
            print(task)

    def write(self) -> None:
        with open(file_name, "w") as file:
            json.dump(self.all_tasks, file, indent=4)

    def load(self) -> None:
        try:
            with open(file_name, "r") as file:
                self.all_tasks = json.load(file)
        except FileNotFoundError:
            self.all_tasks = {}


class Interface:
    """
    Manage user interface.
    """

    def __init__(self) -> None:
        self.options = ["Add Task", "Update Task", "View Tasks With Filter", "Delete Task", "Save And Exit"]
        self.task_manager = TaskManager()
        self.task_manager.load()

    def print_options(self):
        for index, option in enumerate(self.options):
            print(f"{index + 1} - {option}")

    def add_task(self):
        try:
            id = int(input("Enter task ID: "))
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            status = input("Enter task status (e.g., Pending, In Progress, Completed): ")
            task = Task(id, title, description, due_date, status)
            self.task_manager.add_task(task)
        except ValueError:
            print("Invalid input. Task ID must be an integer.")

    def update_task(self):
        try:
            id = int(input("Enter task ID to update: "))
            title = input("Enter new title (or press Enter to skip): ")
            description = input("Enter new description (or press Enter to skip): ")
            due_date = input("Enter new due date (or press Enter to skip): ")
            status = input("Enter new status (or press Enter to skip): ")
            self.task_manager.update_task(id, title or None, description or None, due_date or None, status or None)
        except ValueError:
            print("Invalid input. Task ID must be an integer.")

    def view_tasks(self):
        filterby = input("Enter status to filter by (or press Enter to view all): ")
        self.task_manager.view(filterby or None)

    def delete_task(self):
        try:
            id = int(input("Enter task ID to delete: "))
            self.task_manager.delete_task(id)
        except ValueError:
            print("Invalid input. Task ID must be an integer.")

    def options_handling(self, option):
        match option:
            case 1:
                self.add_task()
            case 2:
                self.update_task()
            case 3:
                self.view_tasks()
            case 4:
                self.delete_task()
            case 5:
                self.task_manager.write()
                print("Tasks saved. Exiting...")
                return False
            case _:
                print("Invalid option, please try again.")
        return True


def main():
    interface = Interface()
    while True:
        interface.print_options()
        try:
            option = int(input(">>> "))
            if option < 1 or option > len(interface.options):
                raise ValueError("Enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 5.")
            continue
        if not interface.options_handling(option):
            break


if __name__ == "__main__":
    main()
