# -*- coding: utf-8 -*-
# LeetCode 541-反转字符串II

"""
Created on Fri Aug 20 21:37 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == 1:
            return s
        if k >= len(s):
            return s[::-1]
        s_r = ''
        n = len(s) // (2 * k)
        s_r += s[k - 1:0:-1]
        s_r += s[0]
        s_r += s[k:2 * k]
        for i in range(1, n):
            s_r += s[k - 1 + i * 2 * k:i * 2 * k - 1:-1]
            s_r += s[k + i * 2 * k:(i + 1) * 2 * k]
        if n != 0:
            if len(s) - n * 2 * k <= k:
                s_r += s[-1:n * 2 * k - 1:-1]
            else:
                s_r += s[k - 1 + n * 2 * k:n * 2 * k - 1:-1]
                s_r += s[k + n * 2 * k:]
        return s_r


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr(s="abcd", k=3))
