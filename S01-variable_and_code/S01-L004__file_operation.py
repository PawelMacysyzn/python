import os

path = r'c:\temp\test.txt' # the "temp" folder must exist on "drive C"

# Sorry i prefer polish content :)
text ='''Utwórz funkcję, która jako parametr przyjmuje ścieżkę dostępu do
pliku i zwraca ilość słów w tym pliku, jeśli potrzebujesz kroków
pomocniczych oto i one:
- Otwórz plik poleceniem open (możesz skorzystać z parametru encoding="utf-16" jeżeli trzeba)
- Wczytaj plik do zmiennej korzystając z funkcji read()
- "Rozbij" wczytaną zawartość korzystając z funkcji split()
- Policz ile elementów jest zwracanych przez funkcję split()
- Zwróć tą wartość'''


def print_content(str_var):
    print(str_var)

def print_infos(str_var, path):
    print("There are {} words in the file {}".format(return_count_words(str_var), path))

def return_count_words(str_var):
    return len(str_var.split())



if os.path.isfile(path):
    print("File {} exists".format(path))
    with open(path, 'r',encoding="utf-16") as f:
        content = f.read()
    # f.close()   # unnecessary
else:
    print("Creating a file {}, and filing with text".format(path))
    with open(path, 'x',encoding="utf-16") as f:
        f.write(text)        
    # f.close() # unnecessary


# print_content(content)
os.path.isfile(path) and print_infos(content, path)