# -*- coding: utf-8 -*-
# LeetCode 859-亲密字符串

"""
Created on Tues Nov 23 18:32 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(goal)
        if len(s) != n:
            return False
        diff_s = set()
        diff_g = set()
        diff = 0
        for i in range(n):
            if s[i] != goal[i]:
                if diff == 2:
                    return False
                diff_s.add(s[i])
                diff_g.add(goal[i])
                diff += 1
        return (diff == 2 and diff_s == diff_g) or (diff == 0 and len(set(goal)) < n)


if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings(s="aaaaaaabc", goal="aaaaaaacb"))
