# -*- coding: utf-8 -*-
# LeetCode 442-数组中重复的数据

"""
Created on Sun May 8 10:04 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]
            else:
                ans.append(num)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([1]))
