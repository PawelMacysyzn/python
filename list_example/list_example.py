

class SingleLinkedList:

    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        return Iterator(self)

    def append(self, item):

        if not self.head:
            self.head = Node(item)
        else:
            i = self.head        # Not None
            while(i.next):       # uNTILL None
                i = i.next
            # import pdb; pdb.set_trace()
            i.next = Node(item)
            # pdb.set_trace()

    def __len__(self):
        counter = 0
        for item in self:
            counter += 1

        return counter

    def clear(self):
        pass

    def extend(self, second_list):
        pass

    def deep_copy(self, target):
        pass

    def remove(self, by_value):
        """
        It's Greeady, remove all ocuranses of value
        """
        # import pdb
        # pdb.set_trace()  # tak testuje sie kod w cmd

        if (self.head):

            ops = self.head
            recon = self.head

            while(ops):
                if(ops.value != by_value):
                    break
                elif(ops.next is None):
                    self.head = None
                    return None

                ops = ops.next

            while(recon):

                if(recon.value == by_value):
                    ops.next = recon.next
                else:  # 2 != 2
                    ops = recon

                recon = recon.next

        else:
            raise IndexError("Its not posible from empty list! ")


class Node:

    # value = None
    # next = None

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Iterator:

    def __init__(self, obj: SingleLinkedList) -> None:
        self.obj = obj

    def __next__(self):
        if self.obj.head is None:
            raise StopIteration()

        value = self.obj.head.value
        self.obj.head = self.obj.head.next

        return value

    def __iter__(self):
        return self


# sll = SingleLinkedList()
# nodeone = Node(1)
# nodetwo = Node(2)


# sll.head = nodeone
# nodeone.next = nodetwo


sll = SingleLinkedList()
nodeone = Node(1)
nodetwo = Node(2)
nodethre = Node(3)
nodefour = Node(2)
nodefive = Node(5)

sll.head = nodeone
nodeone.next = nodetwo
nodetwo.next = nodethre
nodethre.next = nodefour
nodefour.next = nodefive


iterAtor = Iterator(sll)

'''
for item in sll:
    print(item)

# 1
# 2
# 3
# 2
# 5
'''