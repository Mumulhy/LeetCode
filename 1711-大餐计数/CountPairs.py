# -*- coding: utf-8 -*-
# LeetCode 1711-大餐计数

"""
Created on Fri Jul 7 19:48 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count_delicious = {}
        most_delicious = 0
        for delicious in deliciousness:
            if delicious in count_delicious:
                count_delicious[delicious] += 1
            else:
                count_delicious[delicious] = 1
            if delicious > most_delicious:
                most_delicious = delicious
        count_delicious = dict(sorted(count_delicious.items()))
        count_pairs = 0
        for i in range(len(bin(most_delicious)) - 1):
            big_meal = 2 ** i
            for delicious1 in count_delicious:
                delicious2 = big_meal - delicious1
                if delicious2 in count_delicious:
                    if delicious2 > delicious1:
                        count_pairs += count_delicious[delicious1] * count_delicious[delicious2]
                    elif delicious2 == delicious1:
                        count_pairs += count_delicious[delicious1] * (count_delicious[delicious1] - 1) // 2
        return count_pairs % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.countPairs([149, 107, 1, 63, 0, 1, 6867, 1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]))
