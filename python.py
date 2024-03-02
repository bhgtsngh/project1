
import json
import os
from datetime import datetime

class ToDoManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)

    def show_tasks(self):
        print("Your To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['description']} - Priority: {task['priority']}, Due Date: {task['due_date']}")

    def add_task(self, description, priority, due_date):
        task = {
            "description": description,
            "priority": priority,
            "due_date": due_date
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def update_task(self, task_index, new_description, new_priority, new_due_date):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task["description"] = new_description
            task["priority"] = new_priority
            task["due_date"] = new_due_date
            self.save_tasks()
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            self.save_tasks()
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")


if __name__ == "__main__":
    todo_manager = ToDoManager()

    while True:
        print("\nMenu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_manager.show_tasks()
        elif choice == "2":
            description = input("Enter task description: ")
            priority = input("Enter priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_manager.add_task(description, priority, due_date)
        elif choice == "3":
            task_index = int(input("Enter the task index to update: "))
            new_description = input("Enter new task description: ")
            new_priority = input("Enter new priority (High/Medium/Low): ")
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            todo_manager.update_task(task_index, new_description, new_priority, new_due_date)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            todo_manager.delete_task(task_index)
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
