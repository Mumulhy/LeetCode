# -*- coding: utf-8 -*-
# LeetCode 768-最多能完成排序的块II

"""
Created on Sat Aug 13 08:59 2022

@author: _Mumu
Environment: py38
"""

# from collections import defaultdict
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for a in arr:
            if len(stack) == 0 or a >= stack[-1]:
                stack.append(a)
            else:
                mx = stack.pop()
                while stack and stack[-1] > a:
                    stack.pop()
                stack.append(mx)
        return len(stack)

        # sorted_arr = sorted(arr)
        # ans = 0
        # curr_d = defaultdict(int)
        # for i in range(len(arr)):
        #     curr_d[arr[i]] += 1
        #     if curr_d[arr[i]] == 0:
        #         curr_d.pop(arr[i])
        #     curr_d[sorted_arr[i]] -= 1
        #     if curr_d[sorted_arr[i]] == 0:
        #         curr_d.pop(sorted_arr[i])
        #     if not curr_d:
        #         ans += 1
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxChunksToSorted([2, 1, 3, 4, 4]))
