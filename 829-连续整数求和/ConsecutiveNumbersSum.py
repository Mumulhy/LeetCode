# -*- coding: utf-8 -*-
# LeetCode 829-连续整数求和

"""
Created on Fri Jun 3 10:18 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        n *= 2
        ans = 1
        k = 2
        while k * (k + 1) <= n:
            if n % k == 0 and (n // k + k - 1) & 1 == 0:
                ans += 1
            k += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.consecutiveNumbersSum(998875370))
