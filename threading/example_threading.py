import threading
from turtle import begin_fill


begin = 1
scope = 5
nr = 0

def print_num(var_sec,begin,nr):
    print("Thread nr: ",nr)
    for n in range(begin, var_sec+1):
        print(str(n))
        if nr > 4:
            break
        if n == 4:
            nr+=1
            ta = threading.Thread(target=print_num, args=[scope,begin,nr]).start()

if True:
    ta = threading.Thread(target=print_num, args=[scope,begin,nr]).start()
    # ta = threading.Thread(target=print_num, args=(scope,)).start()

# ta.start()


