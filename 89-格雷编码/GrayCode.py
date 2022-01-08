# -*- coding: utf-8 -*-
# LeetCode 89-格雷编码

"""
Created on Sat Jan 8 11:20 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        half_seq = self.grayCode(n - 1)
        diff = 1 << (n - 1)
        return half_seq + [diff + x for x in half_seq[::-1]]

    # def __init__(self):
    #     self.n = 0
    #     self.pow = []
    #     self.gray = [0]
    #     self.left = set()
    #
    # def grayCode(self, n: int) -> List[int]:
    #     self.n = n
    #     self.pow = [pow(2, i) for i in range(n + 1)]
    #     self.gray = [0] * self.pow[-1]
    #     self.left = {i for i in range(1, pow(2, n))}
    #     self.generate(0)
    #     return self.gray
    #
    # def generate(self, j: int) -> None:
    #     if j == self.pow[-1] - 1:
    #         if not self.checkDiff(self.gray[0], self.gray[-1]):
    #             self.gray[-1] = 0
    #         return
    #     x = self.gray[j]
    #     for i in range(self.n):
    #         if (x >> i) & 1 == 0:
    #             take = x + self.pow[i]
    #         else:
    #             take = x - self.pow[i]
    #         if take in self.left:
    #             self.left.remove(take)
    #             self.gray[j + 1] = take
    #             self.generate(j + 1)
    #             if self.gray[-1] != 0:
    #                 return
    #             self.left.add(take)
    #             self.gray[j + 1] = 0
    #
    # def checkDiff(self, a: int, b: int) -> bool:
    #     big = max(a, b)
    #     small = min(a, b)
    #     diff = big - small
    #     return diff in self.pow and (small // diff) & 1 == 0


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(4))
