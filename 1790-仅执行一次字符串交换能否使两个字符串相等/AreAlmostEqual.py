# -*- coding: utf-8 -*-
# LeetCode 1790-仅执行一次字符串交换能否使两个字符串相等

"""
Created on Tues Oct 11 10:19 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if (n := len(s1)) != len(s2):
            return False
        no_match = []
        for i in range(n):
            if s1[i] != s2[i]:
                no_match.append(i)
                if len(no_match) > 2:
                    return False
        if (l := len(no_match)) == 0:
            return True
        if l == 1:
            return False
        return s1[no_match[0]] == s2[no_match[1]] and s1[no_match[1]] == s2[no_match[0]]


if __name__ == '__main__':
    s = Solution()
    print(s.areAlmostEqual(s1="abcd", s2="dcba"))
