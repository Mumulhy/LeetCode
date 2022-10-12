# -*- coding: utf-8 -*-
# LeetCode 817-链表组件

"""
Created on Wed Oct 12 09:31 2022

@author: _Mumu
Environment: py39
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        last_in_arr = False
        ans = 0
        p = head
        while p:
            if p.val in nums:
                if not last_in_arr:
                    last_in_arr = True
                    ans += 1
            else:
                last_in_arr = False
            p = p.next
        return ans
