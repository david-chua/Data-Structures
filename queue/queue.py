# import sys
# sys.path.insert(1,'../doubly_linked_list')
#
# from doubly_linked_list import ListNode
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Single_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements? use linked list
        self.storage = Single_linked_list()

    # insert at the end of the linked list
    def enqueue(self, item):
        new_node = Node(item)
        if self.storage.head == None:
            self.storage.head = new_node
            self.storage.tail = new_node
        else:
            self.storage.tail.next = new_node
            self.storage.tail = new_node
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            return None
        return_value = self.storage.head.value
        if self.size == 1:
            self.storage.head = None
            self.storage.tail = None
        else:
            self.storage.head = self.storage.head.next
        self.size -= 1
        return return_value


    def len(self):
        return self.size
