# -*- coding: utf-8 -*-
# LeetCode 504-七进制数

"""
Created on Mon Mar 7 09:45 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        is_neg = num < 0
        num = abs(num)
        ans = ''
        while num:
            ans += str(num % 7)
            num //= 7
        if is_neg:
            ans += '-'
        return ans[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.convertToBase7(-7))
