# -*- coding: utf-8 -*-
# LeetCode 219-存在重复元素II

"""
Created on Wed Jan 19 08:56 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        s = set()
        for i in range(len(nums)):
            if i > k:
                s.remove(nums[i - k - 1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False

        # if k == 0:
        #     return False
        # last = {}
        # for i, num in enumerate(nums):
        #     if num in last and i - last[num] <= k:
        #         return True
        #     last[num] = i
        # return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
