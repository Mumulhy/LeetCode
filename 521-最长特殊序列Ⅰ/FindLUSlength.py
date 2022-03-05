# -*- coding: utf-8 -*-
# LeetCode 521-最长特殊序列Ⅰ

"""
Created on Sat Mar 5 23:43 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1
