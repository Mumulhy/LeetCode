# -*- coding: utf-8 -*-
# LeetCode 面试题17.09-第 k 个数

"""
Created on Wed Sept 28 09:47 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0] * (k + 1)
        dp[1] = 1
        p3 = p5 = p7 = 1
        for i in range(2, k + 1):
            num3, num5, num7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            dp[i] = min(num3, num5, num7)
            if num3 == dp[i]:
                p3 += 1
            if num5 == dp[i]:
                p5 += 1
            if num7 == dp[i]:
                p7 += 1
        return dp[k]


if __name__ == '__main__':
    s = Solution()
    print(s.getKthMagicNumber(7))
