# -*- coding: utf-8 -*-
# LeetCode 1823-找出游戏的获胜者

"""
Created on Wed May 4 10:49 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 1
        for i in range(2, n + 1):
            winner = (k + winner - 1) % i + 1
        return winner

        # if n == 1:
        #     return 1
        # x = (k + self.findTheWinner(n - 1, k)) % n
        # return n if x == 0 else x


if __name__ == '__main__':
    s = Solution()
    print(s.findTheWinner(6, 5))
