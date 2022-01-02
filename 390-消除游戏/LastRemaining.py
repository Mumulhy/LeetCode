# -*- coding: utf-8 -*-
# LeetCode 390-消除游戏

"""
Created on Sun Jan 2 14:20 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        if n == 3:
            return 2
        return self.lastRemaining(n // 4) * 4 if (n // 2) & 1 == 1 else self.lastRemaining(n // 4) * 4 - 2

        # step, a1, d = 0, 1, 1
        # while n > 1:
        #     if step & 1 == 0:
        #         a1 += d
        #     else:
        #         if n & 1 == 1:
        #             a1 += d
        #     step += 1
        #     d <<= 1
        #     n >>= 1
        # return a1

if __name__ == '__main__':
    s = Solution()
    for i in range(1, 21):
        print(i, s.lastRemaining(i))
