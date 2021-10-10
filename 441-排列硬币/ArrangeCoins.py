# -*- coding: utf-8 -*-
# LeetCode 441-排列硬币

"""
Created on Sun Oct 10 21:15 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1 + 8 * n) ** 0.5) / 2)


if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(15))
