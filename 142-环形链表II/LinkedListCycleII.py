# -*- coding: utf-8 -*-
# LeetCode 142-环形链表II

"""
Created on Thu Oct 3 14:47 2019

@author: _Mumu
Environment: py37
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        step = head
        run = head
        while run and run.next:
            step = step.next           # step步长为1
            run = run.next.next        # run步长为2
            if step is run:            # 检测相遇
                break

        if run and run.next:
            p1 = head
            p2 = run
            while(1):
                if p1 is p2:
                    return p1
                p1 = p1.next           # p1步长为1
                p2 = p2.next           # p2步长为1
        else:
            return None

        # 以下为遍历列表并存储每个元素进行比较的算法

        # NodeList = []
        # step = head
        # while step:
        #     if step in NodeList:
        #         return step
        #     NodeList.append(step)
        #     step = step.next
        # return None