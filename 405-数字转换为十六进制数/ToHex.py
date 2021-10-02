# -*- coding: utf-8 -*-
# LeetCode 405-数字转换为十六进制数

"""
Created on Sat Oct 2 23:00 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def toHex(self, num: int) -> str:
        HEX = '0123456789abcdef'
        numHex = ''
        if num >= 0:
            while num >= 16:
                numHex += HEX[num % 16]
                num //= 16
            numHex += HEX[num]
        else:
            num = -num - 1
            while num >= 16:
                numHex += HEX[15 - num % 16]
                num //= 16
            numHex += HEX[15 - num]
            numHex += 'f' * (8 - len(numHex))
        return numHex[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.toHex(-256))
