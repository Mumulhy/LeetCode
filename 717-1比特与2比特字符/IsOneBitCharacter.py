# -*- coding: utf-8 -*-
# LeetCode 717-1比特与2比特字符

"""
Created on Sat Feb 19 15:03 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        k = n - 2
        while k >= 0:
            if bits[k] == 0:
                break
            k -= 1
        num = n - 2 - k
        return num & 1 == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isOneBitCharacter([0, 1, 1, 1, 1, 0]))
