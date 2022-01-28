# -*- coding: utf-8 -*-
# LeetCode 1996-游戏中弱角色的数量

"""
Created on Fri Jan 28 11:09 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        max_def = 0
        for _, defense in properties:
            if max_def > defense:
                ans += 1
            else:
                max_def = defense
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfWeakCharacters([[1, 5], [10, 4], [4, 3]]))
