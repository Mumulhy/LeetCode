# -*- coding: utf-8 -*-
# LeetCode 166-分数到小数

"""
Created on Sun Oct 3 23:00 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        if (numerator >= 0 and denominator >= 0) or (numerator < 0 and denominator < 0):
            isNeg = False
        else:
            isNeg = True
        numerator, denominator = abs(numerator), abs(denominator)
        mod = [(numerator % denominator) * 10]
        dec = []
        start = -1
        while mod[-1]:
            nowDec = mod[-1] // denominator
            nowMod = (mod[-1] % denominator) * 10
            dec.append(str(nowDec))
            if nowMod in mod:
                start = mod.index(nowMod)
                break
            mod.append(nowMod)
        if start == -1:
            decPos = str(numerator // denominator) + '.' + ''.join(dec)
        else:
            decPos = str(numerator // denominator) + '.' + ''.join(dec[:start]) + '(' + ''.join(dec[start:]) + ')'
        if isNeg:
            return '-' + decPos
        return decPos


if __name__ == '__main__':
    s = Solution()
    print(s.fractionToDecimal(-3, -4))
