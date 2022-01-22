# -*- coding: utf-8 -*-
# LeetCode 1332-删除回文子序列

"""
Created on Sat Jan 22 16:05 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
