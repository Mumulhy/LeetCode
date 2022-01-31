# -*- coding: utf-8 -*-
# LeetCode 1342-将数字变成0的操作次数

"""
Created on Mon Jan 31 11:03 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        b = bin(num)[2:]
        return b.count('1') + len(b) - 1


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSteps(14))
