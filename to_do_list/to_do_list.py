
from re import T


user_choice = 0

tasks = []


def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task was added !")


def delete_task():
    task_indx = int(input("Enter the index of the task to be deleted: "))

    if task_indx < 0 or task_indx > (len(tasks) - 1):
        print("!!! A task with this index does not exist !!!")
        return

    tasks.pop(task_indx)
    print("Task was deleted")


def save_task_to_file():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()


def load_task_from_file():
    try:
        file = open("tasks.txt")

        for line in file.readlines():
            tasks.append(line.strip("\n"))

        file.close()
    except FileNotFoundError:
        return

# ----------------my program---------------------------
load_task_from_file()

while(user_choice != 5):
    if user_choice == 1:
        show_tasks()

    if user_choice == 2:
        add_task()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_task_to_file()

    print()
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save changes to file")
    print("5. Exit")
    print("---------------------------")

    user_choice = int(input("Choice number: "))
