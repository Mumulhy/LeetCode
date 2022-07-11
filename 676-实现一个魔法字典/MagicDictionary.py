# -*- coding: utf-8 -*-
# LeetCode 676-实现一个魔法字典

"""
Created on Mon Jul 11 10:35 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class MagicDictionary:
    def __init__(self):
        self.dictionary = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary = dictionary
        return

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        for word in self.dictionary:
            if len(word) != n:
                continue
            i = 0
            while i < n and word[i] == searchWord[i]:
                i += 1
            if i == n:
                continue
            if word[i + 1:] == searchWord[i + 1:]:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
