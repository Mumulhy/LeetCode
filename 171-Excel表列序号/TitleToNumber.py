# -*- coding: utf-8 -*-
# LeetCode 171-Excel表列序号

"""
Created on Fri Jun 29 14:22 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0
        for i in range(len(columnTitle)):
            columnNumber += (ord(columnTitle[-i - 1]) - 64) * 26 ** i
        return columnNumber


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('ZY'))
