import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=2)

def show_menu():
    print("\n📋 To-Do List Menu:")
    print("1. Show all tasks")
    print("2. Add a new task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def list_tasks(tasks):
    if not tasks:
        print("The task list is empty.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {status} {task['title']}")

def add_task(tasks):
    title = input("🔹 Enter the new task title: ")
    tasks.append({"title": title, "done": False})
    print("✅ Task added.")

def mark_done(tasks):
    list_tasks(tasks)
    if tasks:
        try:
            num = int(input("🔹 Enter the number of the completed task: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print("✅ Task status updated.")
            else:
                print("⛔️ Invalid task number.")
        except ValueError:
            print("⛔️ Please enter a valid number.")

def delete_task(tasks):
    list_tasks(tasks)
    if tasks:
        try:
            num = int(input("🔹 Enter the number of the task to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f" Task '{removed['title']}' deleted.")
            else:
                print("⛔️ Invalid task number.")
        except ValueError:
            print("⛔️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("🟢 Your choice (1-5): ")
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("✅ Changes saved.")
            break
        else:
            print("⛔️ Invalid choice.")

if __name__ == "__main__":
    main()