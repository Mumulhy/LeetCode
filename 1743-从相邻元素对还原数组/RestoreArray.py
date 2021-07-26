# -*- coding: utf-8 -*-
# LeetCode 1743-从相邻元素对还原数组

"""
Created on Sun Jul 25 12:10 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        count_nodes = defaultdict(list)
        for adjacentPair in adjacentPairs:
            count_nodes[adjacentPair[0]].append(adjacentPair[1])
            count_nodes[adjacentPair[1]].append(adjacentPair[0])
        for node in count_nodes:
            if len(count_nodes[node]) == 1:
                head = node
                break
        nums = [head]
        head = count_nodes[head][0]
        nums.append(head)
        while len(count_nodes[head]) == 2:
            for node in count_nodes[head]:
                if node != nums[-2]:
                    nums.append(node)
                    head = node
                    break
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.restoreArray([[4, -2], [1, 4], [-3, 1]]))
