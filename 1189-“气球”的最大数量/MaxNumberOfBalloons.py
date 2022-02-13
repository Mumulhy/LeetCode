# -*- coding: utf-8 -*-
# LeetCode 1189-“气球”的最大数量

"""
Created on Sun Feb 13 10:24 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        return min(cnt['b'], cnt['a'], cnt['l'] // 2, cnt['o'] // 2, cnt['n'])


if __name__ == '__main__':
    s = Solution()
    print(s.maxNumberOfBalloons("leetcode"))
