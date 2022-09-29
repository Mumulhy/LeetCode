# -*- coding: utf-8 -*-
# LeetCode 面试题01.09-字符串轮转

"""
Created on Fri Sept 29 10:29 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in s1 + s1

        # if s1 == s2:
        #     return True
        # if Counter(s1) != Counter(s2):
        #     return False
        # for i in range(len(s1)):
        #     if s1[i:] + s1[:i] == s2:
        #         return True
        # return False


if __name__ == '__main__':
    s = Solution()
    print(s.isFlipedString(s1="waterbottle", s2="erbottlewat"))
