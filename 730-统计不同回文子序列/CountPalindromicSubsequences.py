# -*- coding: utf-8 -*-
# LeetCode 730-统计不同回文子序列

"""
Created on Fri Jun 10 10:53 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        next = [[0] * 4 for _ in range(n)]
        pre = [[0] * 4 for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        pos = [-1] * 4

        for i in range(n):
            for c in range(4):
                pre[i][c] = pos[c]
            pos[ord(s[i]) - ord('a')] = i

        pos[0] = pos[1] = pos[2] = pos[3] = n

        for i in range(n - 1, -1, -1):
            for c in range(4):
                next[i][c] = pos[c]
            pos[ord(s[i]) - ord('a')] = i

        for sz in range(2, n + 1):
            for j in range(sz - 1, n):
                i = j - sz + 1
                if s[i] == s[j]:
                    low, high = next[i][ord(s[i]) - ord('a')], pre[j][ord(s[i]) - ord('a')]
                    if low > high:
                        dp[i][j] = (2 + dp[i + 1][j - 1] * 2) % MOD
                    elif low == high:
                        dp[i][j] = (1 + dp[i + 1][j - 1] * 2) % MOD
                    else:
                        dp[i][j] = (dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]) % MOD
                else:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
        return dp[0][n - 1]
