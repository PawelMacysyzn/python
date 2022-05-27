set_to_choice = ['load data', 'export data', 'analyze & predict']

def prit_option():
    print("------------"*4)
    for count, choice in enumerate(set_to_choice):
        print("{} - {}".format(count, choice))

def display_option(option):
    print("you have selected:\n[ {} - {} ]".format(option,set_to_choice[option]))


def select_option():
    select = input("Select option above or press enter to exit: ")
    try:
        if select.isnumeric():
            if int(select) >= 0 and int(select) < 3:
                display_option(int(select))
            else:
                print("!!! The selected option is not in the above range !!!\n")
        else:
            if not select:
                print("------Exit------")
                return True
            print("The value entered is not a number")
    except:
        print("something really went really bad <lol> XD")
        return True   


while True:
    prit_option()
    if select_option():
        break



