# -*- coding: utf-8 -*-
# LeetCode 1455-检查单词是否为句中其他单词的前缀

"""
Created on Sun Aug 21 15:35 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i = 0
        n = len(sentence)
        m = len(searchWord)
        cnt = 1
        while i < n:
            if sentence[i:i + m] == searchWord:
                return cnt
            while i < n and sentence[i] != ' ':
                i += 1
            i += 1
            cnt += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.isPrefixOfWord(sentence="i am tired", searchWord="you"))
