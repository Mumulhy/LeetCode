# -*- coding: utf-8 -*-
# LeetCode 1282-用户分组

"""
Created on Fri Aug 12 09:46 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for i, group_size in enumerate(groupSizes):
            groups[group_size].append(i)
        ans = []
        for i, group in groups.items():
            ans.extend([group[j:j + i] for j in range(0, len(group), i)])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.groupThePeople([2, 1, 3, 3, 3, 2]))
