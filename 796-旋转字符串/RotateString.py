# -*- coding: utf-8 -*-
# LeetCode 796-旋转字符串

"""
Created on Thu Apr 7 10:12 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        for i in range(1, len(s)):
            if s[:i] == goal[-i:] and s[i:] == goal[:-i]:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.rotateString(s="abcde", goal="cdeab"))
