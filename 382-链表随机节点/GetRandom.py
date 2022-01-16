# -*- coding: utf-8 -*-
# LeetCode 382-链表随机节点

"""
Created on Sun Jan 16 20:01 2022

@author: _Mumu
Environment: py38
"""

# from random import choice
from random import randrange
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        p = self.head
        i = 1
        ans = 0
        while p:
            if randrange(i) == 0:
                ans = p.val
            p = p.next
            i += 1
        return ans

    # def __init__(self, head: Optional[ListNode]):
    #     nodes = {head}
    #     self.vals = [head.val]
    #     p = head
    #     while p.next:
    #         p = p.next
    #         if p not in nodes:
    #             nodes.add(p)
    #             self.vals.append(p.val)
    #
    # def getRandom(self) -> int:
    #     return choice(self.vals)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
