# -*- coding: utf-8 -*-
# LeetCode 2028-找出缺失的观测数据

"""
Created on Sun Mar 27 12:08 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_missing = (m + n) * mean - sum(rolls)
        if sum_missing // n < 1 or sum_missing / n > 6:
            return []
        base = sum_missing // n
        left = sum_missing % n
        return [base] * (n - left) + [base + 1] * left


if __name__ == '__main__':
    s = Solution()
    print(s.missingRolls(rolls=[1], mean=3, n=1))
