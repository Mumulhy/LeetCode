# -*- coding: utf-8 -*-
# LeetCode 940-不同的子序列II

"""
Created on Fri Oct 14 11:28 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [1] * n
        letters = [-1] * 26
        letters[ord(s[0]) - ord('a')] = 0
        for i in range(1, n):
            for j in range(26):
                if letters[j] >= 0:
                    dp[i] = (dp[i] + dp[letters[j]]) % MOD
            letters[ord(s[i]) - ord('a')] = i
        return sum(dp[idx] for idx in letters if idx >= 0) % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.distinctSubseqII('aaa'))
