# -*- coding: utf-8 -*-
# LeetCode 138-复制带随机指针的链表

"""
Created on Thu Jul 22 10:14 2021

@author: _Mumu
Environment: py38
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node' or None:
        if not head:
            return None
        p = head
        while p:
            p.next = Node(p.val, p.next)
            p = p.next.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            else:
                p.next.random = None
            p = p.next.next
        p = head
        head = head.next
        while p:
            p_new = p.next
            if p.next.next:
                p.next = p.next.next
                p_new.next = p_new.next.next
            else:
                p.next = None
                p_new.next = None
            p = p.next
        return head
