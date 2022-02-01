# -*- coding: utf-8 -*-
# LeetCode 1763-最长的美好子字符串

"""
Created on Tues Feb 1 23:14 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        maxPos, maxLen = 0, 0

        def dfs(start, end):
            nonlocal maxPos, maxLen
            if start >= end:
                return
            lower, upper = 0, 0
            for i in range(start, end + 1):
                if s[i].islower():
                    lower |= 1 << (ord(s[i]) - ord('a'))
                else:
                    upper |= 1 << (ord(s[i]) - ord('A'))
            if lower == upper:
                if end - start + 1 > maxLen:
                    maxPos, maxLen = start, end - start + 1
                return
            pos, valid = start, lower & upper
            while pos <= end:
                start = pos
                while pos <= end and valid & (1 << (ord(s[pos].lower()) - ord('a'))):
                    pos += 1
                dfs(start, pos - 1)
                pos += 1

        dfs(0, len(s) - 1)
        return s[maxPos: maxPos + maxLen]


if __name__ == '__main__':
    s = Solution()
    print(s.longestNiceSubstring("HkhBubUYy"))
