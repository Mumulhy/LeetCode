# -*- coding: utf-8 -*-
# LeetCode 645-错误的集合

"""
Created on Fri Jul 4 22:47 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def findErrorNums(self, nums: list) -> list:
        n = len(nums)
        num1 = list(set(range(1, n + 1)) - set(nums))[0]
        return [sum(nums) - (1 + n) * n // 2 + num1, num1]


if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums([1, 2, 2, 4]))
