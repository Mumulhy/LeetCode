# -*- coding: utf-8 -*-
# LeetCode 953-验证外星语词典

"""
Created on Tues May 17 13:58 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = dict(zip(order, range(26)))

        def compare(word1: str, word2: str) -> bool:
            m, n = len(word1), len(word2)
            min_len = min(m, n)
            if word1[:min_len] == word2[:min_len]:
                return m <= n
            for i in range(min_len):
                if word1[i] != word2[i]:
                    return dictionary[word1[i]] < dictionary[word2[i]]

        for i in range(len(words) - 1):
            if compare(words[i], words[i + 1]) is False:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
