# -*- coding: utf-8 -*-
# LeetCode 面试题01.05-一次编辑

"""
Created on Fri May 13 10:23 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if first == second:
            return True
        if abs((m := len(first)) - (n := len(second))) > 1:
            return False
        i, j = 0, 0
        while i < m and j < n:
            if first[i] != second[j]:
                if m == n:
                    return first[i + 1:] == second[j + 1:]
                elif m > n:
                    return first[i + 1:] == second[j:]
                else:
                    return first[i:] == second[j + 1:]
            else:
                i += 1
                j += 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.oneEditAway("pale", "palek"))
