# -*- coding: utf-8 -*-
# LeetCode 面试题17.10-主要元素

"""
Created on Fri Jul 9 16:02 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        global candidate
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        if count == 0:
            return -1
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
        if count > 0:
            return candidate
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
