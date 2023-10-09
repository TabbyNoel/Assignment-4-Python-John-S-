import datetime

# Enum for Priorities
class Priority:
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

# Dictionary to store tasks
tasks = {}

def add_task(title, description, priority, due_date, tags):
    """Add a task to the tasks dictionary."""
    if title in tasks:
        print("Error: A task with this title already exists!")
        return
    tasks[title] = {
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "tags": tags
    }
    print(f"Task '{title}' added successfully!")

def view_tasks():
    """View all tasks."""
    for title, task_data in tasks.items():
        print("-" * 40)
        print(f"Title: {title}")
        print(f"Description: {task_data['description']}")
        print(f"Priority: {task_data['priority']}")
        print(f"Due Date: {task_data['due_date'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Tags: {', '.join(task_data['tags'])}")
    print("-" * 40)

def delete_task(title):
    """Delete a task."""
    if title not in tasks:
        print("Error: No task with this title!")
        return
    del tasks[title]
    print(f"Task '{title}' deleted successfully!")

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter Task Title: ")
            description = input("Enter Task Description: ")
            priority = input("Enter Task Priority (low, medium, high): ").lower()
            while priority not in [Priority.LOW, Priority.MEDIUM, Priority.HIGH]:
                print("Invalid priority!")
                priority = input("Enter Task Priority (low, medium, high): ").lower()
            due_date_str = input("Enter Due Date (YYYY-MM-DD HH:MM:SS): ")
            due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d %H:%M:%S')
            tags_input = input("Enter Tags (comma-separated): ")
            tags = set(tags_input.split(","))
            add_task(title, description, priority, due_date, tags)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            title = input("Enter Task Title to Delete: ")
            delete_task(title)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
