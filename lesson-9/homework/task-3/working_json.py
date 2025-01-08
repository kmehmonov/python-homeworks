import json
import csv

def load_tasks(filename):
    """Load tasks from a JSON file."""
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def save_tasks(filename, tasks):
    """Save tasks to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def calculate_stats(tasks):
    """Calculate and display task completion statistics."""
    total_tasks = len(tasks)
    completed_tasks = sum(task['completed'] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Completion Stats:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def convert_to_csv(json_filename, csv_filename):
    """Convert JSON data to a CSV file."""
    tasks = load_tasks(json_filename)
    if not tasks:
        return

    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

# Main program
def main():
    json_filename = r"lesson-9\homework\task-3\tasks.json"
    csv_filename = r"lesson-9\homework\task-3\tasks.csv"

    # Load tasks from JSON file
    tasks = load_tasks(json_filename)
    
    # Display tasks
    if tasks:

        # Calculate and display stats
        calculate_stats(tasks)

        # Convert to CSV
        convert_to_csv(json_filename, csv_filename)

        # Example of modifying a task
        tasks[0]['completed'] = True
        save_tasks(json_filename, tasks)

if __name__ == "__main__":
    main()
