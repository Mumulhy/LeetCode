# -*- coding: utf-8 -*-
# LeetCode 944-删列造序

"""
Created on Thu May 12 09:47 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))

        # ans = 0
        # for j in range(len(strs[0])):
        #     for i in range(len(strs) - 1):
        #         if strs[i][j] > strs[i + 1][j]:
        #             ans += 1
        #             break
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minDeletionSize(["zyx", "wvu", "tsr"]))
