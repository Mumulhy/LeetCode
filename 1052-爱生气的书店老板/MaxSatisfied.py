# -*- coding: utf-8 -*-
# LeetCode 1052-爱生气的书店老板

"""
Created on Wed Apr 7 21:55 2021

@author: _Mumu
Environment: py37
"""


class Solution:
    def maxSatisfied(self, customers: list, grumpy: list, X: int) -> int:
        n = len(customers)
        total = 0
        for i in range(n):
            if grumpy[i] == 0:
                total += customers[i]
        max_increase = 0
        for i in range(X):
            max_increase += customers[i] * grumpy[i]
        increase = max_increase
        for i in range(n - X):
            increase -= customers[i] * grumpy[i]
            increase += customers[i + X] * grumpy[i + X]
            if increase > max_increase:
                max_increase = increase
        return total + max_increase

        # 超出时间限制惹
        # import numpy as np
        # customers_np = np.array(customers)
        # max_ctm = 0
        # for i in range(len(grumpy) - X + 1):
        #     grumpy_np = np.array(grumpy)
        #     for j in range(X):
        #         grumpy_np[j + i] = 0
        #     grumpy_np ^= 1
        #     now_ctm = np.dot(customers_np, grumpy_np)
        #     if now_ctm > max_ctm:
        #         max_ctm = now_ctm
        # return max_ctm


if __name__ == '__main__':
    s = Solution()
    print(s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
