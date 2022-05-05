# -*- coding: utf-8 -*-
# LeetCode 713-乘积小于 K 的子数组

"""
Created on Thu May 5 09:38 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, product, i = 0, 1, 0
        for j, num in enumerate(nums):
            product *= num
            while i <= j and product >= k:
                product //= nums[i]
                i += 1
            ans += j - i + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
