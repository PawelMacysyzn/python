import pyfirmata2
import time


board = pyfirmata2.Arduino("COM1")


while True:
    board.digital[1].write(1)
    time.sleep(1)
    board.digital[1].write(0)
    time.sleep(1)