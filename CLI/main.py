import sys
import os

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f'Added task: "{task}"')
    
def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f'Deleted task: "{removed_task["task"]}"')
    else:
        print(f"Invalid task index: {index}")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f'Completed task: "{tasks[index]["task"]}"')
    else:
        print(f"Invalid task index: {index}")

def show_tasks():
    if not tasks:
        print("No tasks.")
        return

    for i, task in enumerate(tasks):
        status = "done" if task["completed"] else "pending"
        print(f'{i}. {task["task"]} [ {status} ]')

def main():
    while True:
        print('\t\tSelect command')
        print('1. add task\n2. delete task\n3. complete task\n4. show tasks\n5. quit')
        command = input("Enter command: ")

        if command == '1':
            task = input("Enter task: ").strip()
            add_task(task)
        elif command == '2':
            index = int(input("Enter task index to delete: ").strip())
            delete_task(index)
        elif command == '3':
            index = int(input("Enter task index to complete: ").strip())
            complete_task(index)
        elif command == '4':
            show_tasks()
        elif command == '5':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid command.")
            
        os.system("pause")
        os.system("cls")

if __name__ == "__main__":
    main()
