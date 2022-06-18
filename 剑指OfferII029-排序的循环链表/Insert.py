# -*- coding: utf-8 -*-
# LeetCode 剑指OfferII029-排序的循环链表

"""
Created on Sat Jun 18 10:22 2022

@author: _Mumu
Environment: py38
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        if head.next == head:
            head.next = Node(insertVal, head.next)
            return head
        cur = head
        nxt = head.next
        while nxt is not head:
            if cur.val <= insertVal <= nxt.val:
                break
            if cur.val > nxt.val:
                if insertVal > cur.val or insertVal < nxt.val:
                    break
            cur = cur.next
            nxt = nxt.next
        cur.next = Node(insertVal, nxt)
        return head

        # if not head:
        #     node = Node(insertVal)
        #     node.next = node
        #     return node
        # if head.next == head or head.val == insertVal:
        #     head.next = Node(insertVal, head.next)
        #     return head
        # last = None
        # curr = head
        # p = head
        # pass_by = False
        # while curr.val > insertVal and not pass_by:
        #     last = curr
        #     curr = curr.next
        #     if curr is head:
        #         pass_by = True
        #     if curr.val < last.val:
        #         p = last
        # if pass_by:
        #     p.next = Node(insertVal, p.next)
        #     return head
        # while curr.val < insertVal and not pass_by:
        #     last = curr
        #     curr = curr.next
        #     if curr is head:
        #         pass_by = True
        #     if curr.val < last.val:
        #         p = last
        # if pass_by and head.val < insertVal:
        #     p.next = Node(insertVal, p.next)
        #     return head
        # last.next = Node(insertVal, curr)
        # return head
