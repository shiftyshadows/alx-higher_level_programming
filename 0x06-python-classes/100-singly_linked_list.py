#!/usr/bin/python3
""" Singly Linked Lists module.

This module contains methods about the creation and hendling of
SinglyLinkedList and Node objects.

"""


class Node:
    """ Defines a node of a singly linked list. """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()


# Test the SinglyLinkedList class
if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.sorted_insert(5)
    singly_linked_list.sorted_insert(3)
    singly_linked_list.sorted_insert(7)
    singly_linked_list.sorted_insert(1)
    singly_linked_list.sorted_insert(6)

    print(singly_linked_list)
