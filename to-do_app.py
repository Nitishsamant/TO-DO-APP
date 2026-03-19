import json
from datetime import datetime

tasks = []

# ---------- FILE HANDLING ----------
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except:
        tasks = []

# ---------- CORE FEATURES ----------
def add_task():
    task_name = input("Enter task: ")
    priority = input("Priority (Low/Medium/High): ").capitalize()
    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except:
        print("⚠️ Invalid date format!")
        return

    tasks.append({
        "task": task_name,
        "done": False,
        "priority": priority,
        "due": due_date
    })

    save_tasks()
    print("✅ Task added successfully!")

def view_tasks(filter_type=None):
    if not tasks:
        print("📭 No tasks available.")
        return

    for i, task in enumerate(tasks):
        if filter_type == "done" and not task["done"]:
            continue
        if filter_type == "pending" and task["done"]:
            continue

        status = "✅" if task["done"] else "❌"
        print(f"{i+1}. {task['task']} | {status} | {task['priority']} | Due: {task['due']}")

def mark_done():
    try:
        index = int(input("Task number: ")) - 1
        tasks[index]["done"] = True
        save_tasks()
        print("✅ Marked as done!")
    except:
        print("⚠️ Invalid input!")

def delete_task():
    try:
        index = int(input("Task number: ")) - 1
        removed = tasks.pop(index)
        save_tasks()
        print(f"🗑️ Deleted: {removed['task']}")
    except:
        print("⚠️ Invalid input!")

# ---------- EXTRA FEATURES ----------
def search_tasks():
    keyword = input("Enter keyword: ").lower()
    found = False

    for i, task in enumerate(tasks):
        if keyword in task["task"].lower():
            print(f"{i+1}. {task['task']}")

            found = True

    if not found:
        print("❌ No matching tasks found.")

def sort_tasks():
    tasks.sort(key=lambda x: (x["done"], x["priority"]))
    print("🔃 Tasks sorted!")

# ---------- MENU ----------
def main():
    load_tasks()

    while True:
        print("\n📋 Advanced To-Do App")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Completed Tasks")
        print("4. View Pending Tasks")
        print("5. Mark Task Done")
        print("6. Delete Task")
        print("7. Search Task")
        print("8. Sort Tasks")
        print("9. Exit")

        choice = input("Choose: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks("done")
        elif choice == '4':
            view_tasks("pending")
        elif choice == '5':
            mark_done()
        elif choice == '6':
            delete_task()
        elif choice == '7':
            search_tasks()
        elif choice == '8':
            sort_tasks()
        elif choice == '9':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice!")

main()