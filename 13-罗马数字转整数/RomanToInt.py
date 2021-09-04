# -*- coding: utf-8 -*-
# LeetCode 13-罗马数字转整数

"""
Created on Fri Sept 3 21:53 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lastIs = {'I': False, 'X': False, 'C': False}
        num = 0
        for letter in s:
            num += roman[letter]
            if lastIs['I'] and letter in 'VX':
                num -= 2
                lastIs['I'] = False
            if lastIs['X'] and letter in 'LC':
                num -= 20
                lastIs['X'] = False
            if lastIs['C'] and letter in 'DM':
                num -= 200
                lastIs['C'] = False
            if letter in 'IXC':
                lastIs[letter] = True
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))
