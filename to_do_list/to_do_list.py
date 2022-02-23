from ast import Pass
from ctypes import FormatError
import os
import sys  # end all program

from posixpath import split
tasks = []  # list [task_row_1, task_row2 ..]

# Format tasks
# [2] Pisanie kodu        Priority: (6)    Place: HOME     Status: IN PROGRES


def show_tasks():
    if len(tasks) > 0:
        for num, task in enumerate(tasks):
            print("[" + str(num) + "] " + task[0] +
                  "\tPriority: (" + task[1] + ")" +
                  "\t Place: " + task[2] +
                  "\t Status: " + task[3])
    else:
        print('There is no tasks')


def add_task():
    task_row = []
    task = input("Enter the activity: ")
    task_row.append(task)

    task = input("Choose priority <1 .. 6>: ")
    while (not(int(task) >= 1 and int(task) <= 6)):  # if not <1 .. 6>
        print("Incorect priority!")
        task = input("Choose priority: <1 .. 6>")
    task_row.append(task)

    task = input("Choose place work or home:  W / H: ")
    while (not(task.upper() == "W" or task.upper() == "H")):
        print("Invalid selection!")
        task = input("Choose place work or home:  W / H: ")

    if(task.upper() == "W"):
        task_row.append("WORK")
    else:
        task_row.append("HOME")

    task = input(
        "Choose status \"done\" / \"in progres\" / \"to do\"  D / I / T: ")
    while (not(task.upper() == "D" or task.upper() == "I" or task.upper() == "T")):
        print("Invalid selection!")
        task = input(
            "Choose status \"done\" / \"in progres\" / \"to do\"  D / I / T: ")

    if(task.upper() == "D"):
        task_row.append("DONE")

    elif(task.upper() == "I"):
        task_row.append("IN PROGRES")

    else:
        task_row.append("TO DO")

    tasks.append(task_row)
    print("Task was added !")


def delete_task():
    if len(tasks) > 0:
        delete_task_exit = True
        while(delete_task_exit):
            print("Write \"SHOW\" to display the tasks")
            print("Press \"R\" to exit")

            task_indx = input("Enter the index of the task to be deleted: ")

            if (task_indx.isnumeric() == True):
                task_indx = int(task_indx)
                os.system('cls')
                if task_indx >= 0 and task_indx < len(tasks):
                    tasks.pop(task_indx)
                    print("Task was deleted\n")
                else:
                    print("!!! A task with this index does not exist !!!\n")
            elif (task_indx.capitalize() == 'R'):
                delete_task_exit = False
                os.system('cls')
            elif (task_indx.upper() == 'SHOW'):
                os.system('cls')
                show_tasks()
                print()
            else:
                print('task id has to be numeric, provide correct value')
    else:
        print('There is nothing to remove')


def save_tasks_to_file():
    if len(tasks) > 0:
        print("If you want to quit, enter \"QUIT\"")
        name_file = input("Enter name for file.txt: ")
        if(not(name_file.upper() == "QUIT")):
            with open(name_file, "w") as file:
                for task_row in tasks:
                    for task in task_row:
                        file.write(task + ",    ")
                    file.write("\n")
            print("Save done")
        else:
            pass
    else:
        print('There is nothing to save')


def load_tasks_from_file():
    while(True):
        try:
            print("---------------------------------------------")
            print("If you wanna quit, press \"Q\"")
            print("If you not wanna indicate the file, press \"R\"")

            name_file = input("Indicate the file name.txt: ")

            if(name_file.upper() == "Q"):
                sys.exit(0)

            if(name_file.upper() == "R"):
                break

            with open(name_file) as file:
                lines = file.readlines()
            print("File was opened: ")

            for task_row in lines:
                temp = task_row.strip().strip(",").split(",    ")
                tasks.append(temp)
            break
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
os.system('cls')
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
