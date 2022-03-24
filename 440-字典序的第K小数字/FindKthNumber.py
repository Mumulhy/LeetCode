# -*- coding: utf-8 -*-
# LeetCode 440-字典序的第K小数字

"""
Created on Wed Mar 23 14:26 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        while k:
            steps = self.get_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr

    def get_steps(self, curr: int, n: int) -> int:
        steps, first, last = 0, curr, curr
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps
