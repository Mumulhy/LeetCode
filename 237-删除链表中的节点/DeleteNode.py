# -*- coding: utf-8 -*-
# LeetCode 237-删除链表中的节点

"""
Created on Mon Nov 2 21:05 2021

@author: _Mumu
Environment: py38
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nodeNext = node.next.next
        node.val = node.next.val
        del node.next
        node.next = nodeNext
        return
