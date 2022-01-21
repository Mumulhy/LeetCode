# -*- coding: utf-8 -*-
# LeetCode 1345-跳跃游戏IV

"""
Created on Fri Jan 21 10:24 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        if n == len(set(arr)):
            return n - 1
        closed, stack, new_stack, jumps = set(), set(), set(), set()
        jump_map = defaultdict(set)
        step = 0
        tar = n - 1
        for i, num in enumerate(arr):
            jump_map[num].add(i)
        closed.add(0)
        stack.add(0)
        while True:
            new_stack.update(each + 1 for each in stack)
            new_stack.update(each - 1 for each in stack)
            for each in stack:
                jumps |= jump_map[arr[each]]
                jump_map[arr[each]].clear()
            new_stack |= jumps
            jumps.clear()
            if -1 in new_stack:
                new_stack.remove(-1)
            step += 1
            if tar in new_stack:
                return step
            stack = new_stack - closed
            closed |= new_stack
            new_stack.clear()

        # tar = len(arr) - 1
        # jump_map = defaultdict(list)
        # for i, num in enumerate(arr):
        #     jump_map[num].append(i)
        # closed = set()
        # stack = [0]
        # step = 0
        # while True:
        #     for idx in stack:
        #         if idx == tar:
        #             return step
        #         closed.add(idx)
        #     new_stack = []
        #     for idx in stack:
        #         if idx + 1 <= tar and idx + 1 not in closed:
        #             new_stack.append(idx + 1)
        #         if idx - 1 >= 0 and idx - 1 not in closed:
        #             new_stack.append(idx - 1)
        #         for jump_idx in jump_map[arr[idx]]:
        #             if jump_idx not in closed:
        #                 new_stack.append(jump_idx)
        #         jump_map.pop(arr[idx])
        #     stack = new_stack
        #     step += 1


if __name__ == '__main__':
    s = Solution()
    print(s.minJumps([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))
