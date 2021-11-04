# -*- coding: utf-8 -*-
# LeetCode 367-有效的完全平方数

"""
Created on Thu Nov 4 21:23 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        eps = 1e-6
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            if x0 - x1 <= eps:
                break
            x0 = x1
        return int(x1) ** 2 == num

        # return int(num ** 0.5) ** 2 == num


if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(16))
