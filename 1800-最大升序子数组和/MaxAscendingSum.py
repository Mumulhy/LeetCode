# -*- coding: utf-8 -*-
# LeetCode 1800-最大升序子数组和

"""
Created on Fri Oct 7 11:00 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = curr_sum = last = nums[0]
        for num in nums[1:]:
            if num > last:
                curr_sum += num
                ans = max(ans, curr_sum)
            else:
                curr_sum = num
            last = num
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxAscendingSum([100, 10, 1]))
