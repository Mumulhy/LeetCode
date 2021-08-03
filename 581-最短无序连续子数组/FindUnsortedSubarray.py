# -*- coding: utf-8 -*-
# LeetCode 581-最短无序连续子数组

"""
Created on Tue Aug 3 23:16 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mx = [float('-inf') for _ in range(n + 1)]
        mn = [float('inf') for _ in range(n + 1)]
        for i in range(1, n + 1):
            mx[i] = max(nums[i - 1], mx[i - 1])
        for i in range(n - 1, -1, -1):
            mn[i] = min(nums[i], mn[i + 1])
        l, r = -1, -1
        for i in range(n - 1, -1, -1):
            if mn[i] < mx[i]:
                r = i
                break
        for i in range(n):
            if mx[i] > mn[i]:
                l = i - 1
                break
        if l == -1:
            return 0
        else:
            return r - l + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
