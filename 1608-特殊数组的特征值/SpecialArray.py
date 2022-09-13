# -*- coding: utf-8 -*-
# LeetCode 1608-特殊数组的特征值

"""
Created on Mon Sept 12 15:23 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        keys = sorted(cnt.keys(), reverse=True)
        key = keys[0]
        c = cnt[key]
        for k in keys[1:]:
            if k < c <= key:
                return c
            c += cnt[k]
            key = k
        return c if c <= key else -1


if __name__ == '__main__':
    s = Solution()
    print(s.specialArray([3, 6, 7, 7, 0]))
