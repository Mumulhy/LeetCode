# -*- coding: utf-8 -*-
# LeetCode 961-在长度2N的数组中找出重复N次的元素

"""
Created on Sat May 21 11:31 2022

@author: _Mumu
Environment: py38
"""

from random import randint
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()
        while True:
            idx = randint(0, n - 1)
            if nums[idx] in visited:
                return nums[idx]
            visited.add(nums[idx])
            nums[idx] = nums[-1]
            nums.pop()
            n -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4, 5, 6, 5, 7, 5, 8, 5, 9]))
