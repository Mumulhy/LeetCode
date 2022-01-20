# -*- coding: utf-8 -*-
# LeetCode 2029-石子游戏IX

"""
Created on Thu Jan 20 14:03 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        zero, one, two = 0, 0, 0
        for stone in stones:
            if stone % 3 == 0:
                zero += 1
            elif stone % 3 == 1:
                one += 1
            else:
                two += 1
        zero &= 1
        if zero == 0:
            return one >= 1 and two >= 1
        return one - two > 2 or two - one > 2


if __name__ == '__main__':
    s = Solution()
    print(s.stoneGameIX([5, 1, 2, 4, 3]))
