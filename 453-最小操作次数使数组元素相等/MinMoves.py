# -*- coding: utf-8 -*-
# LeetCode 453-最小操作次数使数组元素相等

"""
Created on Wed Oct 20 15:03 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.minMoves([0, 100, 200]))
