# -*- coding: utf-8 -*-
# LeetCode 面试题01.02-判定是否互为字符重排

"""
Created on Fri Sept 30 11:25 2022

@author: _Mumu
Environment: py39
"""

from collections import Counter


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return Counter(s1) == Counter(s2)
