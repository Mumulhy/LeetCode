# -*- coding: utf-8 -*-
# LeetCode 520-检测大写字母

"""
Created on Sat Nov 13 22:12 2021

@author: _Mumu
Environment: py38
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        secondCapital = word[1].isupper()
        if word[0].islower() and secondCapital:
            return False
        for s in word[2:]:
            if s.isupper() ^ secondCapital:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.detectCapitalUse('faas'))