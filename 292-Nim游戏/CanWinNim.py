# -*- coding: utf-8 -*-
# LeetCode 292-Nim游戏

"""
Created on Sat Sept 18 12:38 2021

@author: _Mumu
Environment: py38
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

if __name__ == '__main__':
    s = Solution()
    print(s.canWinNim(4))