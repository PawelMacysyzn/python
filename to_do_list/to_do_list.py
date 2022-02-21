import os
tasks = []  # list


def show_tasks():
    if len(tasks) > 0:
        for num, task in enumerate(tasks):
            print("[" + str(num) + "] " + task)
    else:
        print('There is no tasks')


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task was added !")


def delete_task():
    task_indx = input("Enter the index of the task to be deleted: ")

    if (task_indx.isnumeric() == True):
        task_indx = int(task_indx)
        if task_indx >= 0 and task_indx < len(tasks):
            tasks.pop(task_indx)
            print("Task was deleted")
        else:
            print("!!! A task with this index does not exist !!!")
    else:
        print('task id has to be numeric, provide correct value')


def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Save done")


def load_tasks_from_file():
    try:
        with open("tasks.txt") as file:
            for line in file.readlines():
                tasks.append(line.strip("\n"))
    except FileNotFoundError:
        print('No previous tasks loaded')


def try_again_message():
    print("\n Wrong value. try again... \n")


def user_choice_to_leave():
    user_choice = 'not answered'
    while(user_choice.capitalize() != 'Y' and user_choice.capitalize() != 'N'):
        user_choice = input("Do you wanna leave program [Y/N]: ")
        if user_choice.capitalize() == "Y":
            return True
        elif user_choice.capitalize() == "N":
            user_choice = 'not answered'
            return False
        else:
            print("Not correct answer")


def print_menu():
    print("---------------------------")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save changes to file")
    print("5. Exit")
    print("---------------------------")


def automatic_save_on_exit():
    user_choice = 'not answered'
    while(user_choice.capitalize() != 'Y' and user_choice.capitalize() != 'N'):
        user_choice = input('Do you wanna save program [Y/N]: ')
        if user_choice.capitalize() == 'Y':
            save_tasks_to_file()
        elif user_choice.capitalize() == 'N':
            pass  # continue
        else:
            print("Not correct answer")
    print("See you soon")


# ----------------my-program---------------------------
load_tasks_from_file()

user_choice = 0
print_menu()
while(user_choice != 5):

    try:
        user_choice = int(input("Choice number: "))
        os.system('cls')
    except ValueError:
        print("Enter correct value again")

    if user_choice == 0:
        print()
        print("Task manager, choice the option ..")

    elif user_choice == 1:
        show_tasks()

    elif user_choice == 2:
        add_task()

    elif user_choice == 3:
        delete_task()

    elif user_choice == 4:
        save_tasks_to_file()

    elif user_choice == 5:
        if user_choice_to_leave():
            break
        else:
            user_choice = 0

    else:
        try_again_message()

    print_menu()

automatic_save_on_exit()
