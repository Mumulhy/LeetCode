# -*- coding: utf-8 -*-
# LeetCode 1015-可被K整除的最小整数

"""
Created on Tues Nov 25 22:36 2025

@author: _Mumu
Environment: py38
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        n, mod = 1, 1
        while mod % k != 0:
            n += 1
            mod = (mod % k) * (10 % k) + 1
        return n

        # if k == 1:
        #     return 1
        # n, mod = 1, 1
        # mods = {1}
        # while mod != 0:
        #     n += 1
        #     mod = (mod * 10 + 1) % k
        #     if mod in mods:
        #         return -1
        #     mods.add(mod)
        # return n
