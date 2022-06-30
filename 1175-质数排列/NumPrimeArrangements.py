# -*- coding: utf-8 -*-
# LeetCode 1175-质数排列

"""
Created on Thu Jun 30 10:49 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        s = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        k = len(s & set(range(1, n + 1)))
        i = max(k, n - k)
        x1, x2 = 1, 1
        while i > 1:
            if i <= k:
                x1 *= i
            if i <= n - k:
                x2 *= i
            i -= 1
        return (x1 * x2) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    print(s.numPrimeArrangements(100))
