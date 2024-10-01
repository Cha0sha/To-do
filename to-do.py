import json
import os

#Opening and editiing the file
#Tasks = add, view , delete , delete all, exit


todoFile = 'todo.json' 

def load_todo():
    if os.path.exists(todoFile):
        with open(todoFile, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:  
                print("Warning: The todo file is corrupted. Loading an empty todo list.")
                return {}
    return {}
def save_todo(todos):
    with open(todoFile, 'w') as f:
        json.dump(todos, f) 

def clear_todos():
    with open(todoFile, 'w') as f:
        json.dump([], f)

def display_todo(todos):
    if not todos:
        print("No tasks assigned.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todos, start=1):
            print(f"{index}: {task}")
    print("\n")

def add_todo(todos):
    task = input("Enter the task: ")  
    todos.append(task)
    save_todo(todos)
    print(f"Added: '{task}' to the to-do list.")

def remove_todo(todos, index):
    if 0 <= index < len(todos):
        removed_todo = todos.pop(index)
        save_todo(todos)
        print(f"Removed: '{removed_todo}' from the list. Thank you.")
    else:
        print("Invalid task number.")

def remove_all_tasks(todos): 
    clear_todos()
    print("All tasks removed. Thank you.")

def main():
    todos = load_todo()

    while True:
        print("Options:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Remove all tasks")
        print("5. Exit")

        choice = input("Choose an option > ")

        if choice == '1':
            add_todo(todos) 
        elif choice == '2':
            display_todo(todos)
        elif choice == '3':
            display_todo(todos)
            try:
                task_number = int(input("Enter the task number to remove: ")) - 1
                remove_todo(todos, task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            remove_all_tasks(todos) 
            todos = [] 
        elif choice == '5':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
