# -*- coding: utf-8 -*-
# LeetCode 1791-找出星型图的中心节点

"""
Created on Fri Feb 18 21:55 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]


if __name__ == '__main__':
    s = Solution()
    print(s.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))
