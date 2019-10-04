# -*- coding: utf-8 -*-
# LeetCode 21-合并两个有序链表

"""
Created on Fri Oct 4 22:27 2019

@author: _Mumu
Environment: py37
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:                       # 其中一个为空链表，直接返回另一个链表
            return l2
        elif not l2:
            return l1

        if l1.val <= l2.val:             # 取结果链表的链表头
            head = l1
        else:
            head = l2

        while l1 and l2:                 # 将一连串比另一边小的节点跳过，接在另一边的前面
            if l1.val <= l2.val:
                while l1.next and l1.next.val <= l2.val:
                    l1 = l1.next
                bridge = l1.next
                l1.next = l2
                l1 = bridge
            else:
                while l2.next and l2.next.val <= l1.val:
                    l2 = l2.next
                bridge = l2.next
                l2.next = l1
                l2 = bridge

        return head