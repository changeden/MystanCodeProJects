"""
File: ds.py
Name: Jerry Liao
------------------------------------
This file shows all the data structures
we built today, including Tree, ListNode, and
PriorityQueue with enqueue, dequeue, traversal,
and length methods.
"""


class Tree:
    def __init__(self, left, value, right):
        self.val = value
        self.right = right
        self.left = left


class ListNode:
    def __init__(self, data, pointer):
        self.val = data
        self.next = pointer


class PriorityQueue:
    def __init__(self, data=None):
        """
        :param data: the first data user wants to input
        """
        self.pq = None
        if data is not None:
            self.pq = ListNode(data, None)

    def enqueue(self, element):
        """
        User call this method to add element to self.pq sorted by element[1]
        :param element: Tuple(Any, int), sort with element[1] for priority queue
        """
        if self.pq is None:
            self.pq = ListNode(element, None)
        else:
            if self.pq.val[1] > element[1]:
                # New node at the beginning
                new_node = ListNode(element, self.pq)
                self.pq = new_node
            else:
                # New node in between
                current = self.pq
                while current.next is not None:
                    if current.val[1] <= element[1] < current.next.val[1]:
                        new_node = ListNode(element, current.next)
                        current.next = new_node
                        break
                    current = current.next
                # New node at the end
                if current.next is None:
                    current.next = ListNode(element, None)

    def dequeue(self):
        """
        Users call this method to get the ListNode with lowest priority
        :return: Tuple[Tree, int], usually called data, with its priority at index 1
        """
        element = self.pq
        self.pq = self.pq.next
        return element.val

    def is_empty(self):
        """
        :return: bool, if self.pq is empty or not
        """
        if self.pq is None:
            return True
        return False

    def traversal_tree_elements(self):
        """
        Users call this method to print out all the element in self.pq
        """
        current = self.pq
        while current is not None:
            if current.next is not None:
                print(current.val[0].val, current.val[1], end=', ')
            else:
                print(current.val[0].val, current.val[1])
            current = current.next
