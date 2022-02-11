# -*- coding: utf-8 -*-
# LeetCode 1447-最简分数

"""
Created on Fri Feb 11 21:25 2022

@author: _Mumu
Environment: py38
"""

# from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return ['{}/{}'.format(j, i) for i in range(2, n + 1) for j in range(1, i) if gcd(i, j) == 1]

        # rela = defaultdict(set)
        # for i in range(2, n + 1):
        #     if not rela[i]:
        #         for j in range(i, n + 1, i):
        #             rela[j].add(i)
        # ans = []
        # for i in range(2, n + 1):
        #     for j in range(1, i):
        #         if not rela[i] & rela[j]:
        #             ans.append('{}/{}'.format(j, i))
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.simplifiedFractions(100))
