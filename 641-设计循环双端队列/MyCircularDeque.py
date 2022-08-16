# -*- coding: utf-8 -*-
# LeetCode 641-设计循环双端队列

"""
Created on Mon Aug 15 09:53 2022

@author: _Mumu
Environment: py39
"""


class Node:
    def __init__(self, val: int, prv: 'Node' = None, nxt: 'Node' = None):
        self.val = val
        self.prv = prv
        self.nxt = nxt


class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.len = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head:
            new_head = Node(value, nxt=self.head)
            self.head.prv = new_head
            self.head = new_head
        else:
            self.head = Node(value)
        if not self.tail:
            self.tail = self.head
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.tail:
            new_tail = Node(value, prv=self.tail)
            self.tail.nxt = new_tail
            self.tail = new_tail
        else:
            self.tail = Node(value)
        if not self.head:
            self.head = self.tail
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        node_to_del = self.head
        if self.len == 1:
            self.head = self.tail = None
            del node_to_del
        else:
            self.head = self.head.nxt
            self.head.prv = None
            del node_to_del
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        node_to_del = self.tail
        if self.len == 1:
            self.head = self.tail = None
            del node_to_del
        else:
            self.tail = self.tail.prv
            self.tail.nxt = None
            del node_to_del
        self.len -= 1
        return True

    def getFront(self) -> int:
        return self.head.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
