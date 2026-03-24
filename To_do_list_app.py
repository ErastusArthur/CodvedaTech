import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        data = json.load(f)
    return data

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_tasks(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print(" Task title cannot be empty.\n")
        return
    task = {
        "title": title,
        "id": len(tasks) + 1,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"{len(tasks)} tasks added.\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
        return
    print("\n---- YOUR TO-DO LIST ----\n")
    for task in tasks:
        status = "Done" if task["done"] else "Pending"
        print(f"{task['id']}.[{status}] {task['title']}")
        print()

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task id: ").strip())
    except ValueError:
        print(f"Invalid input. Please try again.\n")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"No tasks found with ID {task_id} .\n")
        return

    deleted_title = task["title"]
    tasks.remove(task)
    for i, t in enumerate(tasks):
        t["id"] = i + 1
    save_tasks(tasks)
    print(f"Task '{deleted_title}' has been deleted.\n")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task id to mark as done: ").strip())
    except ValueError:
        print("Invalid input. Please try again.\n")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"No tasks found with ID {task_id} .\n")
        return
    if task["done"]:
        print(f"Task {task_id} has been marked as done.\n")
        return

    task["done"] = True
    save_tasks(tasks)
    print(f"Task {task_id} has been marked as done.\n")


def main():
    print("""
    ===============================================================
                                WELCOME 
                        TO DO LIST APPLICATION
    ===============================================================
    """)
    tasks = load_tasks()

    while True:
        print("\n OPTIONS \n")
        print("1. Add task\n")
        print("2. View tasks\n")
        print("3. Delete task\n")
        print("4. Mark tasks as done\n")
        print("5. Quit")

        choice = input("\n Choose an option(1 - 5): ").strip()

        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("It was lovely having you! Good bye.\n")
            break
        else:
            print("Invalid input. Please try again.\n")

main()