# -*- coding: utf-8 -*-
# LeetCode 682-棒球比赛

"""
Created on Sat Mar 26 10:44 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for op in ops:
            if op == '+':
                scores.append(scores[-1] + scores[-2])
            elif op == 'D':
                scores.append(scores[-1] * 2)
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)


if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["1"]))
