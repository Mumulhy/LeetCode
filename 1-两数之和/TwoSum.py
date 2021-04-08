# -*- coding: utf-8 -*-
# LeetCode 1-两数之和

"""
Created on Thu Apr 8 17:41 2021

@author: _Mumu
Environment: py37
"""


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
