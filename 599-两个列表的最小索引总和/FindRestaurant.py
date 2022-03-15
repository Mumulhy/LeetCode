# -*- coding: utf-8 -*-
# LeetCode 599-两个列表的最小索引总和

"""
Created on Mon Mar 14 09:53 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m, n = len(list1), len(list2)
        restaurants = {}
        if m > n:
            list1, list2 = list2.copy(), list1.copy()
        for i, name in enumerate(list1):
            restaurants[name] = i
        ans = []
        min_idx = float('inf')
        for i, name in enumerate(list2):
            if name in restaurants:
                curr_idx = restaurants[name] + i
                if curr_idx < min_idx:
                    ans.clear()
                    min_idx = curr_idx
                    ans.append(name)
                elif curr_idx == min_idx:
                    ans.append(name)
                if i >= min_idx:
                    break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findRestaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
                           list2=["KFC", "Shogun", "Burger King"]))
