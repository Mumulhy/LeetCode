# -*- coding: utf-8 -*-
# LeetCode 532-数组中的k-diff数对

"""
Created on Thu Jun 16 09:46 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_cnt = Counter(nums)
        if k == 0:
            return sum(val > 1 for val in nums_cnt.values())
        vis = set()
        for num in nums_cnt:
            if (another := num + k) in nums_cnt:
                vis.add((num, another))
        return len(vis)


if __name__ == '__main__':
    s = Solution()
    print(s.findPairs(nums=[1, 3, 1, 5, 4], k=0))
