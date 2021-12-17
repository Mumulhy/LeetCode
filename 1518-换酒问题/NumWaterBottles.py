# -*- coding: utf-8 -*-
# LeetCode 1518-换酒问题

"""
Created on Fri Dec 17 11:07 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        num_empty = numBottles
        while num_empty >= numExchange:
            can_exchange = num_empty // numExchange
            ans += can_exchange
            num_empty -= can_exchange * (numExchange - 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numWaterBottles(numBottles=2, numExchange=3))
