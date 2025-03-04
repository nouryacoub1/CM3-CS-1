import json
import os

# File where tasks will be stored
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task, tasks_list):
    """Add a task to the list."""
    tasks_list.append(task)
    save_tasks(tasks_list)
    return tasks_list

def remove_task(task, tasks_list):
    """Remove a task from the list if it exists."""
    if task in tasks_list:
        tasks_list.remove(task)
        save_tasks(tasks_list)
    return tasks_list

def list_tasks(tasks_list):
    """Return the list of tasks."""
    return tasks_list

def main():
    """Main function to run the task manager CLI."""
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager 📋")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks = add_task(task, tasks)
            print(f"Task '{task}' added!")

        elif choice == "2":
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks = remove_task(task, tasks)
                print(f"Task '{task}' removed!")
            else:
                print("Task not found.")

        elif choice == "3":
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks available.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()