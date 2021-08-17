# -*- coding: utf-8 -*-
# LeetCode 413-等差数列划分

"""
Created on Tues Aug 10 16:03 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        now_diff = nums[0] - nums[1]
        now_slice = 1
        slices = 0
        for i in range(1, len(nums) - 1):
            if nums[i] - nums[i + 1] == now_diff:
                now_slice += 1
            else:
                if now_slice >= 2:
                    slices += now_slice * (now_slice - 1) // 2
                now_diff = nums[i] - nums[i + 1]
                now_slice = 1
        if now_slice >= 2:
            slices += now_slice * (now_slice - 1) // 2
        return slices

        # 优化前的代码，内存占用较大
        # if len(nums) <= 2:
        #     return 0
        # diffs = [nums[i] - nums[i + 1] for i in range(len(nums) - 1)]
        # longest_slices = []
        # now_diff = diffs[0]
        # now_slice = 0
        # for diff in diffs:
        #     if diff == now_diff:
        #         now_slice += 1
        #     else:
        #         longest_slices.append(now_slice + 1)
        #         now_diff = diff
        #         now_slice = 1
        # longest_slices.append(now_slice + 1)
        # slices = 0
        # for longest_slice in longest_slices:
        #     if longest_slice >= 3:
        #         slices += (longest_slice - 1) * (longest_slice - 2) // 2
        # return slices


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfArithmeticSlices([1, 2, 3, 4, 6, 8, 10]))
