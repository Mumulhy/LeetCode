# -*- coding: utf-8 -*-
# LeetCode 1713-得到子序列的最少操作次数

"""
Created on Mon Jul 26 11:56 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        target_idx = {}
        for i, num in enumerate(target):
            target_idx[num] = i
        d = []
        for num in arr:
            if num in target_idx:
                if not d or target_idx[num] > d[-1]:
                    d.append(target_idx[num])
                elif target_idx[num] < d[0]:
                    d[0] = target_idx[num]
                elif target_idx[num] not in d:
                    left, right = 0, len(d) - 1
                    while left < right - 1:
                        mid = (left + right) // 2
                        if d[mid] < target_idx[num]:
                            left = mid
                        else:
                            right = mid
                    d[right] = target_idx[num]
        return len(target) - len(d)

        # import bisect
        # target_idx = {}
        # for i, num in enumerate(target):
        #     target_idx[num] = i
        # d = []
        # for num in arr:
        #     if num in target_idx:
        #         idx_lr = bisect.bisect_left(d, target_idx[num])
        #         if idx_lr < len(d):
        #             d[idx_lr] = target_idx[num]
        #         else:
        #             d.append(target_idx[num])
        # return len(target) - len(d)


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(target=[16, 7, 20, 11, 15, 13, 10, 14, 6, 8], arr=[11, 14, 15, 7, 5, 5, 6, 10, 11, 6]))
