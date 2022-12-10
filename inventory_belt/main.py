# A program to select a tool from the inventory bar in the most optimal way
import random
from typing import List


def inventory_bar_optimal_way(start: int, target: int, sieze: int) -> int:
    pass

def inventory_bar_optimal_way_from_random(list: List[str]) -> None:

    bar_len = len(list)
    
    # if bar_len % 2 == 0:
    #     pass # even 
    # else:
    #    pass # odd  

    start = list.index("[_]")
    target = list.index("[x]")


    way_value = target - start
    way_name = None


    if abs(way_value) > bar_len/2:

        if way_value > 0:
            way_value = abs(way_value) - bar_len
        else:
            way_value = way_value + bar_len


    if abs(way_value) == bar_len/2:
        way_name = 'both'
    else:
        if way_value > 0:
            way_name = 'right'
        elif way_value < 0:
            way_name = 'left'
        else:
            raise Exception("Sorry, no move")      


    print(*list, f'-> {way_name}, {abs(way_value)}')
    print(f"{bar_len} elem, start {start}, target {target}  ({target}-{start}) -> {way_value}")



class Dummy_Inventory:
    """
    Static class with methods  
    """

    @staticmethod
    def show_dummy_inventory(repeat: int, size: int) -> None:
        '''
        # Show randomly generates inventory with numbers starting from 0 to (size-1) \n
        # With a random start "_" and target "x" field

        repeat: int -> how many times
        size: int   -> list, starting from 0 to (size-1)
        '''

        for _ in range(repeat):
            print(*Dummy_Inventory.dummy_random_generate_inventory(size))

    @staticmethod
    def dummy_random_generate_inventory(size: int) -> str:
        '''
        Randomly generates inventory with numbers starting from 0 to (size-1) \n
        With a random start "_" and target "x" field
        '''
        list_inventory = Dummy_Inventory.dummy_list_inventory(size)
        start, target = Dummy_Inventory.dummy_random_choice_for_start_and_target(
            list_inventory)

        # replace: start, target
        list_inventory = list(
            map(lambda x: x.replace(start, "[_]"), list_inventory))
        return list(map(lambda x: x.replace(target, "[x]"), list_inventory))

    @staticmethod
    def dummy_random_choice_for_start_and_target(list: List[str]) -> tuple:
        '''
        Randomly generate two non-repeating items from a list
        '''
        list = list.copy()
        start = random.choice(list)
        list.remove(start)
        target = random.choice(list)
        return start, target

    @staticmethod
    def dummy_list_inventory(size: int) -> List[str]:
        '''
        Return list, starting from 0 to (size-1)
        '''
        return [f"[{i}]" for i in range(size)]


'''
[x] [_] -> both, 1
2 elem, start 1, target 0  (0-1) -> -1

[x] [_] -> both, 1
2 elem, start 1, target 0  (0-1) -> -1

[x] [_] -> both, 1
2 elem, start 1, target 0  (0-1) -> -1

[_] [x] -> both, 1
2 elem, start 0, target 1  (1-0) -> 1

[_] [x] -> both, 1
2 elem, start 0, target 1  (1-0) -> 1

[_] [x] -> both, 1
2 elem, start 0, target 1  (1-0) -> 1

[0] [_] [x] -> right, 1
3 elem, start 1, target 2  (2-1) -> 1

[0] [_] [x] -> right, 1
3 elem, start 1, target 2  (2-1) -> 1

[0] [x] [_] -> left, 1
3 elem, start 2, target 1  (1-2) -> -1

[x] [_] [2] -> left, 1
3 elem, start 1, target 0  (0-1) -> -1

[_] [1] [x] -> left, 1
3 elem, start 0, target 2  (2-0) -> -1

[_] [1] [2] [x] [4] -> left, 2
5 elem, start 0, target 3  (3-0) -> -2

[x] [1] [2] [3] [_] -> right, 1
5 elem, start 4, target 0  (0-4) -> 1

[_] [1] [2] [3] [x] -> left, 1
5 elem, start 0, target 4  (4-0) -> -1

[0] [1] [_] [x] [4] -> right, 1
5 elem, start 2, target 3  (3-2) -> 1

[_] [1] [2] [3] [x] -> left, 1
5 elem, start 0, target 4  (4-0) -> -1

[0] [x] [2] [3] [4] [_] -> right, 2
6 elem, start 5, target 1  (1-5) -> 2

[_] [x] [2] [3] [4] [5] -> right, 1
6 elem, start 0, target 1  (1-0) -> 1

[_] [1] [2] [3] [4] [x] -> left, 1
6 elem, start 0, target 5  (5-0) -> -1

[0] [_] [2] [3] [4] [x] -> left, 2
6 elem, start 1, target 5  (5-1) -> -2

[0] [1] [2] [x] [4] [_] [6] -> left, 2
7 elem, start 5, target 3  (3-5) -> -2

[_] [1] [2] [3] [4] [5] [x] -> left, 1
7 elem, start 0, target 6  (6-0) -> -1

[0] [1] [2] [3] [_] [x] [6] -> right, 1
7 elem, start 4, target 5  (5-4) -> 1

[x] [_] [2] [3] [4] [5] [6] -> left, 1
7 elem, start 1, target 0  (0-1) -> -1

[0] [1] [x] [3] [4] [5] [_] -> right, 3
7 elem, start 6, target 2  (2-6) -> 3

[x] [1] [2] [3] [_] [5] [6] -> right, 3
7 elem, start 4, target 0  (0-4) -> 3

[x] [1] [2] [_] [4] [5] [6] -> left, 3
7 elem, start 3, target 0  (0-3) -> -3

[x] [1] [2] [3] [4] [5] [_] -> right, 1
7 elem, start 6, target 0  (0-6) -> 1

[0] [1] [2] [3] [x] [5] [_] -> left, 2
7 elem, start 6, target 4  (4-6) -> -2

[0] [1] [_] [3] [4] [5] [6] [7] [x] [9] -> left, 4
10 elem, start 2, target 8  (8-2) -> -4

[x] [1] [2] [3] [4] [5] [6] [7] [8] [_] -> right, 1
10 elem, start 9, target 0  (0-9) -> 1

[x] [1] [2] [3] [4] [5] [_] [7] [8] [9] -> right, 4
10 elem, start 6, target 0  (0-6) -> 4

[_] [1] [2] [3] [4] [5] [6] [7] [8] [x] -> left, 1
10 elem, start 0, target 9  (9-0) -> -1

[x] [1] [2] [3] [4] [5] [_] [7] [8] [9] [10] -> right, 5
11 elem, start 6, target 0  (0-6) -> 5

[0] [1] [2] [3] [4] [5] [6] [7] [8] [x] [_] -> left, 1
11 elem, start 10, target 9  (9-10) -> -1

[_] [1] [2] [3] [4] [5] [6] [7] [8] [x] [10] -> left, 2
11 elem, start 0, target 9  (9-0) -> -2

[x] [1] [2] [3] [4] [5] [6] [7] [8] [_] [10] -> right, 2
11 elem, start 9, target 0  (0-9) -> 2

[x] [1] [2] [3] [4] [5] [6] [7] [8] [9] [_] -> right, 1
11 elem, start 10, target 0  (0-10) -> 1

[_] [1] [2] [3] [4] [5] [6] [7] [8] [9] [x] -> left, 1
11 elem, start 0, target 10  (10-0) -> -1
'''

'''
Fault

-None-
'''




for _ in range(1000):
    inventory_bar_optimal_way_from_random(Dummy_Inventory.dummy_random_generate_inventory(11))
    print()