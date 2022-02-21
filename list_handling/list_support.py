import random


def random_tab2D(target_tab, size_tab, span):
    row = []
    for i in range(0, size_tab):
        for j in range(0, size_tab):
            row.append(random.randint(0, span))
        target_tab.append(row)
        row = []


def convert_tab_to_int(my_tab_str):
    my_tab_int = []
    for row in my_tab_str:
        temp = []
        for el in row:
            temp.append(int(el))
        my_tab_int.append(temp)
    # or generator
    # my_tab_int = [[int(el) for el in row] for row in my_tab_str]
    return my_tab_int


def print_int_tab2D(my_tab_int):
    for i in range(len(my_tab_int)):
        for j in range(len(my_tab_int)):
            print("%2.0i" % my_tab_int[i][j], end=', ')
        print()
    print("---------------------------------------")


def save_tab_to_file(my_tab):
    with open("list.txt", "w") as file:
        for tab_row in my_tab:
            for tab_colum in tab_row:
                file.write(str(tab_colum) + ", ")
            file.write("\n")
    print("Save done")


def load_tab_from_file():
    my_tab = []
    with open("list.txt") as file:
        lines = file.readlines()

    for i in lines:
        temp = i.strip().strip(",").split(", ")
        my_tab.append(temp)
    return my_tab


def simple_size_tab(my_tab):
    print(my_tab, "\nsize:", len(my_tab))


def size_tab(my_tab):
    print(my_tab, "\nsize:", len(my_tab))
    for i in my_tab:
        print(i, "size:", len(i))
    print("--------------------------------")


my_tab = []

random_tab2D(my_tab, 3, 20)
print_int_tab2D(my_tab)
save_tab_to_file(my_tab)


my_tab = load_tab_from_file()
my_tab = convert_tab_to_int(my_tab)
print_int_tab2D(my_tab)
# print(type(my_tab[1][1]))
