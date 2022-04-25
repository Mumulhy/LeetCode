# -*- coding: utf-8 -*-
# LeetCode 868-二进制间距

"""
Created on Sun Apr 24 10:37 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        dis = 0
        sign = False
        while n:
            if n & 1:
                if sign:
                    ans = max(ans, dis)
                sign = True
                dis = 0
            dis += 1
            n >>= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.binaryGap(9))
