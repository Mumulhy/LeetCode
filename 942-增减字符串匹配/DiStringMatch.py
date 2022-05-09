# -*- coding: utf-8 -*-
# LeetCode 942-增减字符串匹配

"""
Created on Mon May 9 10:10 2022

@author: _Mumu
Environment: py38
"""

from collections import deque
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        q = deque(range(len(s) + 1))
        ans = []
        for ch in s:
            if ch == 'D':
                ans.append(q.pop())
            else:
                ans.append(q.popleft())
        ans.append(q.pop())
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.diStringMatch("DDI"))
