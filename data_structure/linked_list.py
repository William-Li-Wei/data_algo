"""
    deque could be used as LinkedList easily.

    This module also provide a self implementation of linked list.
"""

from collections import deque


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LikedList():
    def __init__(self):
        self.head = None

    def add(self, node: Node):
        if self.head is None:
            self.head = node
        else:
            self.head.next = node
            self.head = node


def test_deque():
    llist = deque('abcde')
    print("init with abcde ->", llist)

    llist.append('f')
    print("append f ->", llist)

    llist.pop()
    print("pop ->", llist)

    llist.appendleft("g")
    print("appendleft g ->", llist)

    llist.popleft()
    print("popleft ->", llist)

    llist.insert(2, 'h')
    print("insert h after idx 2 ->", llist)
