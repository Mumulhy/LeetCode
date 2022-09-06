# -*- coding: utf-8 -*-
# LeetCode 828-统计子串中的唯一字符

"""
Created on Tues Sept 6 09:45 2022

@author: _Mumu
Environment: py39
"""

from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        idx = defaultdict(list)
        for i, ch in enumerate(s):
            idx[ch].append(i)
        ans = 0
        for arr in idx.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                ans += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.uniqueLetterString("LEETCODE"))
