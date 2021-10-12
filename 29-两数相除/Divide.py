# -*- coding: utf-8 -*-
# LeetCode 29-两数相除

"""
Created on Tues Oct 12 20:55 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == -2147483648:
                return 2147483647
            return -dividend
        if (dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0):
            isNeg = False
        else:
            isNeg = True
        if dividend > 0:
            dividend = -dividend
        if divisor > 0:
            divisor = -divisor
        divisors = [0]
        quotients = [0]
        quotient = 1
        while divisor >= dividend:
            divisors.append(divisor)
            quotients.append(quotient)
            divisor += divisor
            quotient += quotient
        divisor = divisors[-1]
        quotient = quotients[-1]
        divisors.pop()
        quotients.pop()
        for div, quo in zip(divisors[::-1], quotients[::-1]):
            if divisor >= dividend - div:
                divisor += div
                quotient += quo
                if divisor == dividend:
                    break
        if isNeg:
            return -quotient
        return quotient


if __name__ == '__main__':
    s = Solution()
    print(s.divide(-2147483647, -2))
