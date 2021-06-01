# -*- coding: utf-8 -*-
# LeetCode 461-汉明距离

"""
Created on Fri Jun 1 20:41 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum([int(i) for i in list(bin(x ^ y))[2:]])

        # 大佬写的更简便写法
        # return bin(x ^ y).count('1')


if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1, 4))
