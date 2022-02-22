from ast import Pass
import os
import sys  # end all program

from posixpath import split
tasks = []  # list [task_row_1, task_row2 ..]

# tasks = [['Granie w gry', '6'], ['Pracowanie na dematic', '1']]


def show_tasks():
    if len(tasks) > 0:
        for num, task in enumerate(tasks):
            print("[" + str(num) + "] " + task[0] +
                  "\t Priority: (" + task[1] + ")")
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

    tasks.append(task_row)
    print("Task was added !")


def delete_task():
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


def save_tasks_to_file():
    print("If you want to quit, enter \"QUIT\"")
    name_file = input("Enter name for file: ")
    if(not(name_file.upper() == "QUIT")):
        with open(name_file + ".txt", "w") as file:
            for task_row in tasks:
                for task in task_row:
                    file.write(task + ",    ")
                file.write("\n")
        print("Save done")
    else:
        pass


def load_tasks_from_file():
    while(True):
        try:
            print("If you wanna quit, press \"Q\"")
            name_file = input("Indicate the file name: ")

            if(name_file.upper() == "Q"):
                sys.exit(0)      

            with open(name_file + ".txt") as file:
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
