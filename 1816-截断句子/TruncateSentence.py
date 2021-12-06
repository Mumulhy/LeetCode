# -*- coding: utf-8 -*-
# LeetCode 1816-截断句子

"""
Created on Mon Dec 6 14:22 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        length = 0
        for i in range(len(s)):
            if s[i] == ' ':
                k -= 1
                if k == 0:
                    length = i
                    break
        if length == 0:
            return s
        return s[:length]


if __name__ == '__main__':
    s = Solution()
    print(s.truncateSentence(s="chopper is not a tanuki", k=5))
