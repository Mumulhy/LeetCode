# -*- coding: utf-8 -*-
# LeetCode 141-环形链表

"""
Created on Thu Oct 3 14:02 2019

@author: _Mumu
Environment: py37
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        step = head
        run = head
        while(1):
            if run is None:
                return False
            elif run.next is None:
                return False
            step = step.next           # step步长为1
            run = run.next.next        # run步长为2
            if step is run:
                return True