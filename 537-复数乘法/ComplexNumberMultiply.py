# -*- coding: utf-8 -*-
# LeetCode 537-复数乘法

"""
Created on Fri Feb 25 11:44 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        re1, im1 = map(int, num1[:-1].split('+'))
        re2, im2 = map(int, num2[:-1].split('+'))
        re = re1 * re2 - im1 * im2
        im = re1 * im2 + re2 * im1
        return ''.join([str(re), '+', str(im), 'i'])


if __name__ == '__main__':
    s = Solution()
    print(s.complexNumberMultiply(num1="1+3i", num2="1+1i"))
