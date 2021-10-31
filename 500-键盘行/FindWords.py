# -*- coding: utf-8 -*-
# LeetCode 500-键盘行

"""
Created on Sun Oct 31 21:12 2021

@author: _Mumu
Environment: py38
"""

from typing import List

lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            wordLower = word.lower()
            n = len(word)
            for line in lines:
                i = 0
                while i < n:
                    if wordLower[i] not in line:
                        break
                    i += 1
                if i == n:
                    ans.append(word)
                    break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["omk"]))
