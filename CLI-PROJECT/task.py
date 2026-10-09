import sys
import json

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []


command = sys.argv[1]

if command == "add":
    task_name = sys.argv[2]
    task = {
        "title" : task_name,
        "completed" : False
    }
    
    tasks.append(task)

    with open("tasks.json", "w") as file:
        json.dump(tasks,file)

        print(f"Tasks added: {task_name}")

elif command == "list":
 for index, task in enumerate(tasks, start=1):
    if task["completed"]:
       print(f"{index}. {task['title']} ✓ ")
    else:
       print(f":{index}. {task['title']}")

elif command == "done":
    task_number = int(sys.argv[2])
    index = task_number - 1

    if index < 0 or index >= len(tasks):
        print("Task not found!")
    else:
        tasks[index]["completed"] = True

        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

        print("Task completed!")

elif  command == "delete":
    task_number = int(sys.argv[2])
    index = task_number - 1

    if index < 0 or index >= len(tasks):
        print("Task not found!")
    else:
        tasks.pop(index)

        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

        print("Task deleted!")
elif command == "sort":
    tasks.sort(key=lambda task: task["completed"])

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

    print("Tasks sorted!")
elif  command == "help":
    print("Available commands:")
    print("add <task> - Add a task")
    print("list - Show all tasks")
    print("done <number> - Complete a task")
    print("delete <number> - Delete a task")
    print("sort - Sort tasks")
    print("help - Show this help")