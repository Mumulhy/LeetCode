# -*- coding: utf-8 -*-
# LeetCode 1220-统计元音字母序列的数目

"""
Created on Mon Jan 17 19:12 2022

@author: _Mumu
Environment: py38
"""


# import numpy as np


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        u, v, w, x, y = 5, 10, 19, 35, 68
        if n == 1:
            return u
        if n == 2:
            return v
        if n == 3:
            return w
        if n == 4:
            return x
        for _ in range(n - 5):
            u, v, w, x, y = v, w, x, y, (u + w + 3 * x) % 1000000007
        return y

        # MOD = 10 ** 9 + 7
        # matrix = np.mat([(0, 1, 1, 0, 1), (1, 0, 1, 0, 0), (0, 1, 0, 1, 0), (0, 0, 1, 0, 0), (0, 0, 1, 1, 0)])
        # ans = np.mat([(1,), (1,), (1,), (1,), (1,)])
        # n -= 1
        # while n > 0:
        #     if n & 1 == 1:
        #         ans = matrix * ans % MOD
        #     matrix = matrix * matrix % MOD
        #     n //= 2
        # return int(ans.sum() % MOD)

        # MOD = 10 ** 9 + 7
        # cnt_last = [1, 1, 1, 1, 1]  # a: 0, e: 1, i: 2, o: 3, u: 4
        # for _ in range(n - 1):
        #     new_cnt_last = [0] * 5
        #     new_cnt_last[0] = (cnt_last[1] + cnt_last[2] + cnt_last[4]) % MOD
        #     new_cnt_last[1] = (cnt_last[0] + cnt_last[2]) % MOD
        #     new_cnt_last[2] = (cnt_last[1] + cnt_last[3]) % MOD
        #     new_cnt_last[3] = cnt_last[2] % MOD
        #     new_cnt_last[4] = (cnt_last[2] + cnt_last[3]) % MOD
        #     cnt_last = new_cnt_last
        # return sum(cnt_last) % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.countVowelPermutation(5))
