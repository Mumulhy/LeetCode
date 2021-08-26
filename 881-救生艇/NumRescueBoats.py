# -*- coding: utf-8 -*-
# LeetCode 881-救生艇

"""
Created on Tues Aug 24 14:30 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            boats += 1
        return boats


if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats(people=[3, 2, 2, 1], limit=3))
