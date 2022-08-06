# -*- coding: utf-8 -*-
# LeetCode 1408-数组中的字符串匹配

"""
Created on Sat Aug 6 08:33 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for s1 in words:
            for s2 in words:
                if s1 == s2:
                    continue
                if s1 in s2:
                    ans.append(s1)
                    break
        return ans
