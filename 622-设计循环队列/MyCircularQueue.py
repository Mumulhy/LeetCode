# -*- coding: utf-8 -*-
# LeetCode 622-设计循环队列

"""
Created on Tues Aug 2 09:35 2022

@author: _Mumu
Environment: py38
"""


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.len, self.max_len = 0, k
        self.head_idx, self.tail_idx = 0, -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.len += 1
        self.tail_idx += 1
        if self.tail_idx == self.max_len:
            self.tail_idx = 0
        self.queue[self.tail_idx] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.len -= 1
        self.head_idx += 1
        if self.head_idx == self.max_len:
            self.head_idx = 0
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head_idx]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail_idx]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.max_len

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
