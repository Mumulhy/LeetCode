# -*- coding: utf-8 -*-
# LeetCode 670-最大交换

"""
Created on Tues Sept 13 10:04 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        maxIdx = n - 1
        idx1 = idx2 = -1
        for i in range(n - 1, -1, -1):
            if s[i] > s[maxIdx]:
                maxIdx = i
            elif s[i] < s[maxIdx]:
                idx1, idx2 = i, maxIdx
        if idx1 < 0:
            return num
        s[idx1], s[idx2] = s[idx2], s[idx1]
        return int(''.join(s))


if __name__ == '__main__':
    s = Solution()
    print(s.maximumSwap(98368))
