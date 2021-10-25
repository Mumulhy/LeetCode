# -*- coding: utf-8 -*-
# LeetCode 638-大礼包

"""
Created on Fri Oct 24 23:25 2021

@author: _Mumu
Environment: py38
"""

from functools import lru_cache
from typing import List, Tuple


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        specialFiltered = []
        for sp in special:
            if sum(sp[:n]) > 0 and sum(sp[i] * price[i] for i in range(n)) > sp[-1]:
                specialFiltered.append(sp)

        @lru_cache(None)
        def calMinPrice(currNeeds: Tuple[int]) -> int:
            minPrice = sum(currNeeds[i] * price[i] for i in range(n))
            for currSpecial in specialFiltered:
                nextNeeds = []
                for i in range(n):
                    if currNeeds[i] < currSpecial[i]:
                        break
                    nextNeeds.append(currNeeds[i] - currSpecial[i])
                if len(nextNeeds) == n:
                    minPrice = min(minPrice, calMinPrice(tuple(nextNeeds)) + currSpecial[-1])
            return minPrice

        return calMinPrice(tuple(needs))


if __name__ == '__main__':
    s = Solution()
    print(s.shoppingOffers(price=[2, 3, 4], special=[[1, 1, 0, 4], [2, 2, 1, 9]], needs=[1, 2, 1]))
