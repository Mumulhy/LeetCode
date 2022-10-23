# -*- coding: utf-8 -*-
# LeetCode 1768-交替合并字符串

"""
Created on Sun Oct 23 15:39 2022

@author: _Mumu
Environment: py38
"""

from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(c1 + c2 for c1, c2 in zip_longest(word1, word2, fillvalue=''))


if __name__ == '__main__':
    s = Solution()
    print(s.mergeAlternately(word1="abcd", word2="pq"))
