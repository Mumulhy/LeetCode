# -*- coding: utf-8 -*-
# LeetCode 229-求众数II

"""
Created on Fri Oct 22 20:33 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num1 = None
        num2 = None
        n1 = 0
        n2 = 0
        for num in nums:
            if num == num1:
                n1 += 1
            elif num == num2:
                n2 += 1
            elif not n1:
                num1 = num
                n1 = 1
            elif not n2:
                num2 = num
                n2 = 1
            else:
                n1 -= 1
                n2 -= 1
        ans = []
        if n1 and nums.count(num1) > n // 3:
            ans.append(num1)
        if n2 and nums.count(num2) > n // 3:
            ans.append(num2)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
