# -*- coding: utf-8 -*-
# LeetCode 168-Excel表列名称

"""
Created on Fri Jun 29 13:45 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ''
        while columnNumber > 0:
            columnNumber -= 1
            title += chr(65 + columnNumber % 26)
            columnNumber //= 26
        return title[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(701))
