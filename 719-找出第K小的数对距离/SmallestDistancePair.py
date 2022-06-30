# -*- coding: utf-8 -*-
# LeetCode 719-找出第K小的数对距离

"""
Created on Thu Jun 30 22:14 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count(mid: int) -> int:
            cnt = i = 0
            for j, num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j - i
            return cnt

        return bisect_left(range(nums[-1] - nums[0]), k, key=count)


if __name__ == '__main__':
    s = Solution()
    print(s.smallestDistancePair(nums=[1, 6, 1], k=3))
