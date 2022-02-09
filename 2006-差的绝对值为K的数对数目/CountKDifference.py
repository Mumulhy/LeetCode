# -*- coding: utf-8 -*-
# LeetCode 2006-差的绝对值为K的数对数目

"""
Created on Wed Feb 9 11:29 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        ans = 0
        for num in nums:
            ans += cnt[num + k] + cnt[num - k]
            cnt[num] += 1
        return ans

        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if abs(nums[i] - nums[j]) == k:
        #             ans += 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countKDifference(nums=[3, 2, 1, 5, 4], k=2))
