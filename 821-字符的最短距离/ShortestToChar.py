# -*- coding: utf-8 -*-
# LeetCode 821-字符的最短距离

"""
Created on Tues Apr 19 11:21 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        stack = []
        ans = [-1] * n
        for i in range(n):
            if s[i] == c:
                stack.append(i)
        dis = 0
        while stack:
            for idx in stack:
                ans[idx] = dis
            new_stack = []
            for idx in stack:
                if idx + 1 < n and ans[idx + 1] == -1:
                    new_stack.append(idx + 1)
                if idx - 1 >= 0 and ans[idx - 1] == -1:
                    new_stack.append(idx - 1)
            stack = new_stack
            dis += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.shortestToChar(s="aaab", c="b"))
