# -*- coding: utf-8 -*-
# LeetCode 556-下一个更大元素III

"""
Created on Sun Jul 3 10:09 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        ss = str(n)
        idx = len(ss) - 1
        prev = '0'
        while idx >= 0 and ss[idx] >= prev:
            prev = ss[idx]
            idx -= 1
        if idx == -1:
            return -1
        suf = list(ss[idx + 1:][::-1])
        i = bisect(suf, ss[idx])
        bri = suf[i]
        suf[i] = ss[idx]
        ans = int(ss[:idx] + bri + ''.join(suf))
        return ans if ans < 2 ** 31 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement(1393605430))
