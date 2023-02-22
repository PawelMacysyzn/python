# python -m unittest -v list_example_test.py
import unittest
from list_example import SingleLinkedList, Node


class TestSingleLinkedList(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.game = SingleLinkedList()

    def test_append_empty_list(self):

        # Arrange

        empty_list = SingleLinkedList()
        node = Node(1)

        # Act

        empty_list.append(1)

        # Assert

        # Object of list must be idicate the node with have same value
        # as node constructed in the arrange step
        # and its next fielld has to idicate none object

        self.assertEqual(empty_list.head.value, 1)

    def test_append_third_elem_to_none_empty_list(self):

        # Arrange

        sll = SingleLinkedList()
        nodeone = Node(1)
        nodetwo = Node(2)

        sll.head = nodeone
        nodeone.next = nodetwo
        nodetwo.next = None

        # Act

        sll.append(3)

        # Assert

        # Object of list must be idicate the node with have same value
        # as node constructed in the arrange step
        # and its next fielld has to idicate none object
        # import pdb; pdb.set_trace()
        self.assertEqual(nodetwo.next.value, 3)
        # pdb.set_trace()

    def test_remove_on_none_empty_list(self):

        # Arrange

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
        # nodefive.next = None // to sie robi z atomatu

        # Act
        sll.remove(2)
        # egzample of debug
        # import pdb; pdb.set_trace()
        # breakpoint()

        # Assert
        self.assertTrue(((nodeone.next is nodethre)
                         and (nodethre.next is nodefive)))

    def test_remove_on_none_empty_list_but_last_element_is_to_be_removed(self):

        # Arrange

        sll = SingleLinkedList()
        nodeone = Node(1)
        nodetwo = Node(2)
        nodethre = Node(3)
        nodefour = Node(2)
        nodefive = Node(5)
        nodesix = Node(2)

        sll.head = nodeone
        nodeone.next = nodetwo
        nodetwo.next = nodethre
        nodethre.next = nodefour
        nodefour.next = nodefive
        nodefive.next = nodesix

        # Act
        sll.remove(2)
        # import pdb; pdb.set_trace()

        # Assert
        self.assertTrue(((nodeone.next is nodethre)
                         and (nodethre.next is nodefive)
                         and (nodefive.next is None)))

    def test_remove_on_none_empty_list_but_doubled_value(self):

        # Arrange

        sll = SingleLinkedList()
        nodeone = Node(1)
        nodetwo = Node(2)
        nodethre = Node(2)
        nodefour = Node(5)
        nodefive = Node(2)

        sll.head = nodeone
        nodeone.next = nodetwo
        nodetwo.next = nodethre
        nodethre.next = nodefour
        nodefour.next = nodefive

        # Act
        # import pdb; pdb.set_trace()
        sll.remove(2)

        # Assert
        self.assertTrue((nodeone.next is nodefour)
                        and (nodefour.next is None))

    # def test_remove_on_list_with_only_one_element_but_last_element_is_to_be_removed(self):

    #     # Arrange

    #     sll = SingleLinkedList()
    #     nodeone = Node(2)

    #     sll.head = nodeone

    #     # Act
    #     # import pdb; pdb.set_trace()
    #     sll.remove(2)

    #     # Assert
    #     self.assertTrue(sll.head is None)

    # def testt_remove_but_not_without_removing(self):

    #     # Arrange

    #     sll = SingleLinkedList()
    #     nodeone = Node(1)

    #     sll.head = nodeone

    #     # Act
    #     sll.remove(2)

    #     # Assert
    #     self.assertTrue((sll.head is None)
    #                     and)
