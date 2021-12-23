# -*- coding: utf-8 -*-
# LeetCode 1044-最长重复子串

"""
Created on Thu Dec 23 11:07 2021

@author: _Mumu
Environment: py38
"""

# from collections import Counter
from random import randint
from typing import List


class Solution:
    def __init__(self):
        self.a1 = 0
        self.a2 = 0
        self.mod1 = 0
        self.mod2 = 0
        self.n = 0

    def longestDupSubstring(self, s: str) -> str:
        self.a1, self.a2 = randint(26, 100), randint(26, 100)
        self.mod1, self.mod2 = randint(10 ** 9 + 7, 2 ** 31 - 1), randint(10 ** 9 + 7, 2 ** 31 - 1)
        self.n = len(s)
        arr = [ord(ch) - ord('a') for ch in s]
        l, r = 1, self.n - 1
        length, start = 0, -1
        while l <= r:
            m = (l + r + 1) // 2
            idx = self._check(arr, m)
            if idx != -1:
                l = m + 1
                length = m
                start = idx
            else:
                r = m - 1
        return s[start:start + length] if start != -1 else ''

    def _check(self, arr: List[int], m: int) -> int:
        a_l1, a_l2 = pow(self.a1, m, self.mod1), pow(self.a2, m, self.mod2)
        h1, h2 = 0, 0
        for i in range(m):
            h1 = (h1 * self.a1 + arr[i]) % self.mod1
            h2 = (h2 * self.a2 + arr[i]) % self.mod2
        seen = {(h1, h2)}
        for start in range(1, self.n - m + 1):
            h1 = (h1 * self.a1 - arr[start - 1] * a_l1 + arr[start + m - 1]) % self.mod1
            h2 = (h2 * self.a2 - arr[start - 1] * a_l2 + arr[start + m - 1]) % self.mod2
            if (h1, h2) in seen:
                return start
            seen.add((h1, h2))
        return -1

        # cnt_s = Counter(s)
        # if max(cnt_s.values()) <= 1:
        #     return ''
        # stack = [s]
        # while True:
        #     new_stack = []
        #     for ss in stack:
        #         new_stack.append(ss[:-1])
        #     new_stack.append(stack[-1][1:])
        #     cnt_sub = Counter(new_stack)
        #     for ss in cnt_sub:
        #         if cnt_sub[ss] > 1:
        #             return ss
        #     stack = new_stack


if __name__ == '__main__':
    s = Solution()
    print(s.longestDupSubstring(s="banana"))
