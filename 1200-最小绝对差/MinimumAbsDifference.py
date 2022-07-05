# -*- coding: utf-8 -*-
# LeetCode 1200-最小绝对差

"""
Created on Mon Jul 4 11:16 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        ans = []
        n = len(arr)
        for i in range(n - 1):
            if (cur_diff := arr[i + 1] - arr[i]) < min_diff:
                ans = [[arr[i], arr[i + 1]]]
                min_diff = cur_diff
            elif cur_diff == min_diff:
                ans.append([arr[i], arr[i + 1]])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
