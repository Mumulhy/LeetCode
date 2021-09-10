# -*- coding: utf-8 -*-
# LeetCode 1894-找到需要补充粉笔的学生编号

"""
Created on Fri Sept 10 20:57 2021

@author: _Mumu
Environment: py38
"""

# from bisect import bisect
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]

        # if chalk[0] > k:
        #     return 0
        # for i in range(1, len(chalk)):
        #     chalk[i] += chalk[i - 1]
        #     if chalk[i] > k:
        #         return i
        # k %= chalk[-1]
        # return bisect(chalk, k)


if __name__ == '__main__':
    s = Solution()
    print(s.chalkReplacer(chalk=[0, 5, 1, 5], k=22))
