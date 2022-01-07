# -*- coding: utf-8 -*-
# LeetCode 1614-括号的最大嵌套深度

"""
Created on Fri Jan 7 11:52 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        left = 0
        res = 0
        for ch in s:
            if ch == '(':
                left += 1
                res = max(res, left)
            elif ch == ')':
                left -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth("(1+(2*3)+((8)/4))+1"))
