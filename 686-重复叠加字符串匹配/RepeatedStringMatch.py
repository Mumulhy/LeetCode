# -*- coding: utf-8 -*-
# LeetCode 686-重复叠加字符串匹配

"""
Created on Wed Dec 22 10:38 2021

@author: _Mumu
Environment: py38
"""

from collections import Counter
from math import ceil


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        cnt_a = Counter(a)
        cnt_b = Counter(b)
        if len(cnt_b) > len(cnt_a):
            return -1
        p = 0
        for ch in cnt_a:
            p = max(p, ceil(cnt_b[ch] / cnt_a[ch]))
        c = a * p
        if b in c:
            return p
        c += a
        p += 1
        return p if b in c else -1


if __name__ == '__main__':
    s = Solution()
    print(s.repeatedStringMatch(a="abc", b="wxyz"))
