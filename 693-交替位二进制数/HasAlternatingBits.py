# -*- coding: utf-8 -*-
# LeetCode 693-交替位二进制数

"""
Created on Mon Mar 28 09:54 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = -1
        while n:
            new_bit = n & 1
            if bit == -1 or bit ^ new_bit:
                bit = new_bit
            else:
                return False
            n >>= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.hasAlternatingBits(10))
