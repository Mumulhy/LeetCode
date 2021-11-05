# -*- coding: utf-8 -*-
# LeetCode 1218-最长定差子序列

"""
Created on Fri Nov 5 23:59 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))
