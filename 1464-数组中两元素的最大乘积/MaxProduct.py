# -*- coding: utf-8 -*-
# LeetCode 1464-数组中两元素的最大乘积

"""
Created on Fri Aug 26 09:59 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([3, 4, 5, 2]))
