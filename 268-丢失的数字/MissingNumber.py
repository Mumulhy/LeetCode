# -*- coding: utf-8 -*-
# LeetCode 268-丢失的数字

"""
Created on Sat Nov 6 14:15 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n):
            xor ^= nums[i] ^ i
        return xor ^ n


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
