# -*- coding: utf-8 -*-
# LeetCode 777-在LR字符串中交换相邻字符

"""
Created on Sun Oct 2 10:50 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i = j = 0
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                c = start[i]
                if c == 'L' and i < j or c == 'R' and i > j:
                    return False
                i += 1
                j += 1
        while i < n:
            if start[i] != 'X':
                return False
            i += 1
        while j < n:
            if end[j] != 'X':
                return False
            j += 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canTransform(start="RXXLRXRXL", end="XRLXXRRLX"))
