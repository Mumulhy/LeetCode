# -*- coding: utf-8 -*-
# LeetCode 剑指Offer52-两个链表的第一个公共节点

"""
Created on Wed Jul 21 11:04 2021

@author: _Mumu
Environment: py38
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode or None:
        if not (headA and headB):
            return None
        pA = headA
        pB = headB
        while pA or pB:
            if not pA:
                pA = headB
            if not pB:
                pB = headA
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        return None
