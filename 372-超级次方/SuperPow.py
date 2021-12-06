# -*- coding: utf-8 -*-
# LeetCode 372-超级次方

"""
Created on Sun Dec 5 23:18 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD
        if a == 1:
            return 1
        a_pow = {0: 1, 1: a}
        for i in range(2, 10):
            if i & 1 == 0:
                a_pow[i] = (a_pow[i // 2] ** 2) % MOD
            else:
                a_pow[i] = (a_pow[i - 1] * a) % MOD
        ans = 1
        for digit in b:
            ans = (pow(ans, 10, MOD) * a_pow[digit]) % MOD
        return ans

        # a %= 1337
        # if a == 1:
        #     return 1
        # a_pow = {0: 1, 1: a}
        # for i in range(2, 10):
        #     if i & 1 == 0:
        #         a_pow[i] = (a_pow[i // 2] ** 2) % 1337
        #     else:
        #         a_pow[i] = (a_pow[i - 1] * a) % 1337
        # ans = 1
        # for digit in b[:-1]:
        #     ans *= a_pow[digit]
        #     ans %= 1337
        #     curr = ans
        #     for _ in range(3):
        #         ans *= ans
        #         ans %= 1337
        #     for _ in range(2):
        #         ans *= curr
        #         ans %= 1337
        # ans *= a_pow[b[-1]]
        # ans %= 1337
        # return ans

    #     if a == 1:
    #         return 1
    #     a %= 1337
    #     ans = 1
    #     for digit in self.toBin(b):
    #         ans *= ans
    #         ans %= 1337
    #         if digit == 1:
    #             ans *= a
    #             ans %= 1337
    #     return ans
    #
    # def toBin(self, large_num: List[int]) -> List[int]:
    #     large_num = large_num[::-1]
    #     large_bin = []
    #     while large_num:
    #         last_left = 0
    #         for i in range(len(large_num) - 1, -1, -1):
    #             if last_left == 1:
    #                 large_num[i] += 10
    #             last_left = large_num[i] & 1
    #             large_num[i] //= 2
    #         large_bin.append(last_left)
    #         if large_num[-1] == 0:
    #             large_num.pop()
    #     return large_bin[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.superPow(a=2147483647, b=[2, 0, 0]))
