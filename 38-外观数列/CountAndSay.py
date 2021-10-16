# -*- coding: utf-8 -*-
# LeetCode 38-外观数列

"""
Created on Fri Oct 15 23:50 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        last = '1'
        curr = ''
        for _ in range(n - 1):
            i = 0
            lastLen = len(last)
            while i < lastLen:
                k = i
                while i < lastLen - 1 and last[i + 1] == last[i]:
                    i += 1
                k = i - k + 1
                curr += str(k) + last[i]
                i += 1
            last = curr
            curr = ''
        return last


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(6))
