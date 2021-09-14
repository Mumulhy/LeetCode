# -*- coding: utf-8 -*-
# LeetCode 524-通过删除字母匹配到字典里最长单词

"""
Created on Tues Sept 14 19:21 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longestWord = ''
        for word in dictionary:
            index = 0
            if len(word) < len(longestWord):
                continue
            for letter in word:
                index = s.find(letter, index) + 1
                if not index:
                    break
            else:
                if len(word) > len(longestWord) or word < longestWord:
                    longestWord = word
        return longestWord

        # n = len(s)
        # f = [[0] * 26 for _ in range(n)]
        # f.append([n] * 26)
        #
        # for i in range(n - 1, -1, -1):
        #     for j in range(26):
        #         if ord(s[i]) == j + 97:
        #             f[i][j] = i
        #         else:
        #             f[i][j] = f[i + 1][j]
        #
        # longestWord = ''
        # for word in dictionary:
        #     i = 0
        #     match = True
        #     if len(word) < len(longestWord):
        #         continue
        #     for letter in word:
        #         if f[i][ord(letter) - 97] == n:
        #             match = False
        #             break
        #         i = f[i][ord(letter) - 97] + 1
        #     if match and (len(word) > len(longestWord) or word < longestWord):
        #         longestWord = word
        #
        # return longestWord

        # dictionary.sort(key=lambda x: (-len(x), x))
        # n = len(s)
        # for word in dictionary:
        #     i = j = 0
        #     wordLen = len(word)
        #     while j < wordLen:
        #         while i < n and s[i] != word[j]:
        #             i += 1
        #         if i == n:
        #             break
        #         i += 1
        #         j += 1
        #     if j == wordLen:
        #         return word
        # return ''

        # longestWord = ''
        # n = len(s)
        # for word in dictionary:
        #     i = j = 0
        #     wordLen = len(word)
        #     if wordLen < len(longestWord):
        #         continue
        #     while j < wordLen:
        #         while i < n and s[i] != word[j]:
        #             i += 1
        #         if i == n:
        #             break
        #         i += 1
        #         j += 1
        #     if j == wordLen and (len(longestWord) < wordLen or word < longestWord):
        #         longestWord = word
        # return longestWord


if __name__ == '__main__':
    s = Solution()
    print(s.findLongestWord(s="abcea", dictionary=["abe", "abc", "clp", 'abce']))
