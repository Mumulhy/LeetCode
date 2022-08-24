# -*- coding: utf-8 -*-
# LeetCode 1460-通过翻转子数组使两个数组相等

"""
Created on Wed Aug 24 11:28 2022

@author: _Mumu
Environment: py39
"""

from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
