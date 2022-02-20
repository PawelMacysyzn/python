user_choice = 0
user_exception = True

tasks = [] # list


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


def try_again_message():
    print()
    print("Wrong value entered")
    print("Try again !\n")


def user_choice_to_leave():
    user_exception = False

    while (not user_exception):
        print("Do you wanna continue: Y / N")
        try:
            user_exception_continue = input()
        except:
            print("Continue")

        if user_exception_continue.capitalize() == "Y":
            user_exception = True
        elif user_exception_continue.capitalize() == "N":
            # terminates the program
            user_choice = 5
            print("See yaa")
            break
        else:
            print("Try again, again xd")

def print_menu():
    print()
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save changes to file")
    print("5. Exit")
    print("---------------------------")


def automatic_save_on_exit():
    print("Do you wanna save program Y/N")
    save_program_loop = True
    while(save_program_loop):
        try:
            user_exception_continue_to_save = input()
        except:
            print("Continue")

        if user_exception_continue_to_save.capitalize() == "Y":
            save_task_to_file()
            save_program_loop = False
        elif user_exception_continue_to_save.capitalize() == "N":
            print("See yaa soon")
            save_program_loop = False
        else:
            print("Try again, again xd")

# ----------------my-program---------------------------
load_task_from_file()

while(user_choice != 5):

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
        save_task_to_file()

    else:
        try_again_message()
        user_choice_to_leave()

    if (user_exception):
        print_menu()
        try:
            user_choice = int(input("Choice number: "))
        except ValueError:
            try_again_message()

automatic_save_on_exit()