# -*- coding: utf-8 -*-
# LeetCode 720-词典中最长的单词

"""
Created on Thu Mar 17 09:55 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)
        candidate = set()
        ans = ''
        ans_len = 0
        for word in words:
            if (l := len(word)) == 1 or word[:-1] in candidate:
                candidate.add(word)
                if l > ans_len or (l == ans_len and word < ans):
                    ans, ans_len = word, l
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
