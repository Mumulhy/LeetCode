# -*- coding: utf-8 -*-
# LeetCode 921-使括号有效的最少添加

"""
Created on Tues Oct 4 10:49 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lefts, rights = 0, 0
        for ch in s:
            if ch == '(':
                lefts += 1
            else:
                if lefts:
                    lefts -= 1
                else:
                    rights += 1
        return lefts + rights


if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid("((("))
