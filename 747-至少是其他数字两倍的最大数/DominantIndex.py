# -*- coding: utf-8 -*-
# LeetCode 747-至少是其他数字两倍的最大数

"""
Created on Thu Jan 13 00:37 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = 0
        idx = 0
        second_largest = 0
        for i in range(len(nums)):
            if nums[i] >= largest:
                second_largest = largest
                largest = nums[i]
                idx = i
            elif nums[i] > second_largest:
                second_largest = nums[i]
        return idx if largest >= 2 * second_largest else -1


if __name__ == '__main__':
    s = Solution()
    print(s.dominantIndex([3, 6, 1, 0]))
