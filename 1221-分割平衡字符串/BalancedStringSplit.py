# -*- coding: utf-8 -*-
# LeetCode 1221-分割平衡字符串

"""
Created on Tues Sept 7 16:58 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        splited = diffLR = 0
        for letter in s:
            if letter == 'L':
                diffLR += 1
            else:
                diffLR -= 1
            if diffLR == 0:
                splited += 1
        return splited


if __name__ == '__main__':
    s = Solution()
    print(s.balancedStringSplit("LLLLRRRR"))
