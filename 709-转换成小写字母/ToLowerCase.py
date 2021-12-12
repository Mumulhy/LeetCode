# -*- coding: utf-8 -*-
# LeetCode 709-转换成小写字母

"""
Created on Sun Dec 12 14:17 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(asc | 32) if 64 < (asc := ord(ch)) < 91 else ch for ch in s)


if __name__ == '__main__':
    s = Solution()
    print(s.toLowerCase('Hello'))
