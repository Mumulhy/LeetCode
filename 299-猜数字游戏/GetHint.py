# -*- coding: utf-8 -*-
# LeetCode 299-猜数字游戏

"""
Created on Mon Nov 8 16:50 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        counts = defaultdict(int)
        for s1, s2 in zip(secret, guess):
            counts[s1] += 1
            if s1 == s2:
                A += 1
        for s2 in guess:
            if counts[s2]:
                counts[s2] -= 1
                B += 1
        B -= A
        return '{}A{}B'.format(A, B)


if __name__ == '__main__':
    s = Solution()
    print(s.getHint(secret="1807", guess="7810"))
