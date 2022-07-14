# -*- coding: utf-8 -*-
# LeetCode 745-前缀和后缀搜索

"""
Created on Thu Jul 14 10:01 2022

@author: _Mumu
Environment: py38
"""

from itertools import zip_longest
from typing import List


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = {}
        self.weight_key = ('#', '#')
        for i, word in enumerate(words):
            cur = self.trie
            m = len(word)
            for j in range(m):
                tmp = cur
                for k in range(j, m):
                    key = (word[k], '#')
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weight_key] = i
                tmp = cur
                for k in range(j, m):
                    key = ('#', word[-k - 1])
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weight_key] = i
                key = (word[j], word[-j - 1])
                if key not in cur:
                    cur[key] = {}
                cur = cur[key]
                cur[self.weight_key] = i

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for key in zip_longest(pref, suff[::-1], fillvalue='#'):
            if key not in cur:
                return -1
            cur = cur[key]
        return cur[self.weight_key]

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
