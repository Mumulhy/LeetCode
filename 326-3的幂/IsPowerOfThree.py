# -*- coding: utf-8 -*-
# LeetCode 326-3的幂

"""
Created on Thu Sept 23 20:19 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

        # power = 1
        # while power < n:
        #     power *= 3
        # return power == n


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(243))
