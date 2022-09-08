# -*- coding: utf-8 -*-
# LeetCode 667-优美的排列II

"""
Created on Thu Sept 8 10:32 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        i = 1
        j = 1 + k
        ans = []
        while j > i:
            ans.append(i)
            ans.append(j)
            i += 1
            j -= 1
        if j == i:
            ans.append(i)
        ans.extend(list(range(ans[1] + 1, n + 1)))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.constructArray(6, 3))
