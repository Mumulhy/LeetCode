# -*- coding: utf-8 -*-
# LeetCode 383-赎金信

"""
Created on Sat Dec 4 09:50 2021

@author: _Mumu
Environment: py38
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_ran = Counter(ransomNote)
        cnt_mag = Counter(magazine)
        return cnt_ran & cnt_mag == cnt_ran


if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct(ransomNote="aa", magazine="aab"))
