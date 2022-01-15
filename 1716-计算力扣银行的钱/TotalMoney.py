# -*- coding: utf-8 -*-
# LeetCode 1716-计算力扣银行的钱

"""
Created on Sat Jan 15 18:04 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        return ((1 + days + 2 * weeks) * days + 7 * (7 + weeks) * weeks) // 2


if __name__ == '__main__':
    s = Solution()
    print(s.totalMoney(20))
