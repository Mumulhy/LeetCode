# -*- coding: utf-8 -*-
# LeetCode 307-区域和检索 - 数组可修改

"""
Created on Mon Apr 4 12:24 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        self.n = len(self.tree)
        for i, num in enumerate(nums, 1):
            self.add(i, num)

    def add(self, index: int, val: int) -> None:
        while index < self.n:
            self.tree[index] += val
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        s = 0
        while index:
            s += self.tree[index]
            index &= index - 1
        return s

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum(right + 1) - self.prefix_sum(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
