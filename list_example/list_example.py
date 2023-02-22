import copy


class SingleLinkedList:

    def __init__(self) -> None:
        self.head = None

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
        pass

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

        recon = self.head  # poczatek
        
        ops = copy.deepcopy(self.head) # Not necessary but only temporary

        while(recon):

            if(recon.value == by_value):
                ops.next = recon.next
            else:  # 2 != 2
                ops = recon

            recon = recon.next

            # if(recon.value == by_value):
            #     if ops.next:
            #         ops.next = recon.next
            #     else:
            #         ops = recon.next
            # else:  # 2 != 2
            #     ops = recon

            # recon = recon.next


class Node:

    # value = None
    # next = None

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# sll = SingleLinkedList()
# nodeone = Node(1)
# nodetwo = Node(2)


# sll.head = nodeone
# nodeone.next = nodetwo
