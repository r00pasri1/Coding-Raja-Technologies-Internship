import json
from datetime import datetime, timedelta

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task_description, priority, due_date_str):
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        task = {
            'description': task_description,
            'priority': priority,
            'due_date': due_date.strftime("%Y-%m-%d"),
            'completed': False
        }

        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task index")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task index")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTask List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_description = input("Enter task description: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")

            todo_list.add_task(task_description, priority, due_date_str)

        elif choice == '2':
            task_index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(task_index)

        elif choice == '3':
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_completed(task_index)

        elif choice == '4':
            todo_list.display_tasks()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
