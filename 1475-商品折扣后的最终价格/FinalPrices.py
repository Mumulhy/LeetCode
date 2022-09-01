# -*- coding: utf-8 -*-
# LeetCode 1475-商品折扣后的最终价格

"""
Created on Thu Sept 1 14:58 2022

@author: _Mumu
Environment: py39
"""

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        stack = [0]
        for i in range(n - 1, -1, -1):
            p = prices[i]
            while stack[-1] > p:
                stack.pop()
            ans[i] = p - stack[-1]
            stack.append(p)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.finalPrices([8, 4, 6, 2, 3]))
