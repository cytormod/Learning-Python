def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Search by Priority")
    print("6. Exit")

def add_task(tasks):
    name = input("Enter task name: ")
    deadline = input("Enter deadline (e.g., 2024-12-31): ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    tasks[name] = {"deadline": deadline, "priority": priority}
    print(f"Task '{name}' added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for name, details in tasks.items():
        print(f"Name: {name}, Deadline: {details['deadline']}, Priority: {details['priority']}")

def edit_task(tasks):
    name = input("Enter the task name to edit: ")
    if name in tasks:
        new_name = input("Enter new task name (leave blank to keep current): ") or name
        deadline = input("Enter new deadline (leave blank to keep current): ") or tasks[name]["deadline"]
        priority = input("Enter new priority (High/Medium/Low, leave blank to keep current): ").capitalize() or tasks[name]["priority"]
        tasks.pop(name)  # Remove old key if name changes
        tasks[new_name] = {"deadline": deadline, "priority": priority}
        print(f"Task '{new_name}' updated successfully!")
    else:
        print(f"Task '{name}' not found.")

def delete_task(tasks):
    name = input("Enter the task name to delete: ")
    if name in tasks:
        tasks.pop(name)
        print(f"Task '{name}' deleted successfully!")
    else:
        print(f"Task '{name}' not found.")

def search_by_priority(tasks):
    priority = input("Enter priority to search (High/Medium/Low): ").capitalize()
    found_tasks = {name: details for name, details in tasks.items() if details["priority"] == priority}
    if found_tasks:
        print(f"\nTasks with priority '{priority}':")
        for name, details in found_tasks.items():
            print(f"Name: {name}, Deadline: {details['deadline']}")
    else:
        print(f"No tasks with priority '{priority}' found.")

def main():
    tasks = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_by_priority(tasks)
        elif choice == "6":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
