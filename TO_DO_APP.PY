import json

tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    save_tasks()

def view_tasks():
    for index, task in enumerate(tasks):
        status = "✅ Done" if task["done"] else "❌ Not Done"
        print(f"{index + 1}. {task['task']} - {status}")

def mark_done():
    index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks()

def delete_task():
    index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()

def main():
    load_tasks()
    while True:
        print("\n📋 To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do App.")
            break
        else:
            print("⚠️ Invalid option, please try again.")

main()
