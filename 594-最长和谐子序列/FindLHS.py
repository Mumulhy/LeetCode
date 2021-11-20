# -*- coding: utf-8 -*-
# LeetCode 594-最长和谐子序列

"""
Created on Sat Nov 20 09:57 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        return max((counts[num] + counts[num + 1] for num in counts if num + 1 in counts), default=0)

        # counts = defaultdict(int)
        # ans = 0
        # for num in nums:
        #     counts[num] += 1
        #     if counts[num + 1] or counts[num - 1]:
        #         ans = max(ans, counts[num] + counts[num + 1], counts[num] + counts[num - 1])
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findLHS([1, 2, 3, 1]))
