# -*- coding: utf-8 -*-
# LeetCode 1601-最多可达成的换楼请求数目

"""
Created on Mon Feb 28 10:55 2022

@author: _Mumu
Environment: py39
"""

from itertools import combinations
from typing import List


# def bit_count(num: int) -> int:
#     if num < 0:
#         num = num & 0xffffffff
#     cnt = 0
#     while num:
#         num &= num - 1
#         cnt += 1
#     return cnt


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        for i in range(len(requests), 0, -1):
            for comb in combinations(requests, i):
                delta = [0] * n
                for x, y in comb:
                    delta[x] -= 1
                    delta[y] += 1
                if all(x == 0 for x in delta):
                    return i
        return 0

        # ans = 0
        # for mask in range((1 << len(requests)) - 1, -1, -1):
        #     bits = bit_count(mask)
        #     if bits <= ans:
        #         continue
        #     delta = [0] * n
        #     for i, (x, y) in enumerate(requests):
        #         if (mask >> i) & 1:
        #             delta[x] -= 1
        #             delta[y] += 1
        #     if all(x == 0 for x in delta):
        #         ans = bits
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumRequests(n=3, requests=[[0, 0], [1, 2], [2, 1]]))
