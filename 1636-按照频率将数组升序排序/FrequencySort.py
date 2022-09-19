# -*- coding: utf-8 -*-
# LeetCode 1636-按照频率将数组升序排序

"""
Created on Mon Sept 19 10:34 2022

@author: _Mumu
Environment: py39
"""

from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return sorted(nums, key=lambda num: (cnt[num], -num))


if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort([1, 2, 2, 3, 3]))
