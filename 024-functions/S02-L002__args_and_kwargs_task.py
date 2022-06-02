
def calculate_paint(efficency_ltr_per_m2, *rooms):

    return efficency_ltr_per_m2 * sum(rooms)
    

list_rooms = [42, 28, 30]
print(calculate_paint(0.25, 42, 28, 30))    # 25.0
print(calculate_paint(0.25, *list_rooms))   # 25.0



def log_it(path, *args):

    with open(path, "a") as f:

        
        for line in args:
            f.write(line)
            f.write(' ')
        f.write('\n')

path = r'c:\temp\log_it.txt'

log_it(path, 'Starting processing forecasting')
log_it(path ,'ERROR', 'Not enough data', 'invoices', '2021')