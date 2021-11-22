# -*- coding: utf-8 -*-
# LeetCode 384-打乱数组

"""
Created on Mon Nov 22 12:53 2021

@author: _Mumu
Environment: py38
"""

# from random import choice
# from random import random
from random import randint
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.origin = nums
        self.len = len(self.origin)
        self.shuffled = []

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        self.shuffled = self.origin.copy()
        for i in range(self.len):
            j = randint(i, self.len - 1)
            self.shuffled[i], self.shuffled[j] = self.shuffled[j], self.shuffled[i]
        return self.shuffled

    # def __init__(self, nums: List[int]):
    #     self.origin = nums
    #
    # def reset(self) -> List[int]:
    #     return self.origin
    #
    # def shuffle(self) -> List[int]:
    #     return sorted(self.origin, key=lambda x: random())

    # def __init__(self, nums: List[int]):
    #     self.origin = nums
    #     self.len = len(self.origin)
    #     self.shuffled = []
    #
    # def reset(self) -> List[int]:
    #     return self.origin
    #
    # def shuffle(self) -> List[int]:
    #     self.shuffled.clear()
    #     idx_list = list(range(self.len))
    #     while idx_list:
    #         idx = choice(idx_list)
    #         idx_list.remove(idx)
    #         self.shuffled.append(self.origin[idx])
    #     return self.shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == '__main__':
    s = Solution([1, 2, 3])
    print(s.shuffle())
    print(s.reset())
    print(s.shuffle())
