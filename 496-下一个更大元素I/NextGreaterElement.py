# -*- coding: utf-8 -*-
# LeetCode 496-下一个更大元素I

"""
Created on Tues Oct 26 18:49 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        p = []
        for num in nums2[::-1]:
            while p and p[-1] < num:
                p.pop()
            nextGreater[num] = p[-1] if p else -1
            p.append(num)
        return [nextGreater[num] for num in nums1]


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
