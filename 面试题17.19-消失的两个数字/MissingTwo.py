# -*- coding: utf-8 -*-
# LeetCode 面试题17.19-消失的两个数字

"""
Created on Mon Sept 26 11:24 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        xor = 0
        n = len(nums) + 2
        for num in nums:
            xor ^= num
        for i in range(1, n + 1):
            xor ^= i
        lsb = xor & (-xor)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        for i in range(1, n + 1):
            if i & lsb:
                type1 ^= i
            else:
                type2 ^= i
        return [type1, type2]


if __name__ == '__main__':
    s = Solution()
    print(s.missingTwo([2]))
