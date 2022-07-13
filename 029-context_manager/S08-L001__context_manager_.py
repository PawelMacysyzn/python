
# try:
#     with open(r'C:\temp\my_file*.txt', 'w+') as file:
#         file.writelines('SUCCESS')
# except OSError as e:
#     print('Error opening file {}, detaails: {}'.format(e.filename, e.strerror))


import time

class time_measure:

    def __init__(self) -> None:
        pass

    def __enter__(self):
        print('entering...')
        self.__start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting...')
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print('Execution time: {}'.format(self.__difference))

    
# with time_measure() as my_timer:
#     time.sleep(3)


with time_measure():
    time.sleep(3)


'''
entering...
exiting...
Execution time: 3.000969886779785
'''







