# -*- coding: utf-8 -*-
# LeetCode 1441-用栈操作构建数组

"""
Created on Sat Oct 15 21:34 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 1
        ans = []
        for num in target:
            while num != i:
                ans.append('Push')
                ans.append('Pop')
                i += 1
            ans.append('Push')
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.buildArray(target=[1, 2], n=4))
