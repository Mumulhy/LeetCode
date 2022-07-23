# -*- coding: utf-8 -*-
# LeetCode 剑指OfferII115-重建序列

"""
Created on Sat Jul 23 10:04 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = defaultdict(set)
        k = set()
        for sequence in sequences:
            k |= set(sequence)
            for i in range(len(sequence) - 1):
                graph[sequence[i]].add(sequence[i + 1])
        if len(k) < (n := len(nums)):
            return False
        for i in range(n - 1):
            if nums[i] in graph and nums[i + 1] in graph[nums[i]]:
                continue
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.sequenceReconstruction(nums=[1, 2, 3], sequences=[[1, 2], [1, 3], [2, 3]]))
