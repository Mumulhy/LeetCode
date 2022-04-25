# -*- coding: utf-8 -*-
# LeetCode 398-随机数索引

"""
Created on Mon Apr 25 09:45 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from random import choice
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = defaultdict(list)
        for i, num in enumerate(nums):
            self.nums[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.nums[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
