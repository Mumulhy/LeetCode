# -*- coding: utf-8 -*-
# LeetCode 905-按奇偶排序数组

"""
Created on Wed Apr 28 10:31 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [num for num in nums if num & 1 == 0] + [num for num in nums if num & 1]


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([0]))
