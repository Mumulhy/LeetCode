# -*- coding: utf-8 -*-
# LeetCode 890-查找和替换模式

"""
Created on Sun Jun 12 14:55 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        curr_map = {}
        curr_vis = set()
        curr_match = True
        ans = []
        for word in words:
            for y, x in zip(word, pattern):
                if x in curr_map:
                    if y != curr_map[x]:
                        curr_match = False
                        break
                else:
                    if y in curr_vis:
                        curr_match = False
                        break
                    curr_map[x] = y
                    curr_vis.add(y)
            if curr_match:
                ans.append(word)
            curr_map.clear()
            curr_vis.clear()
            curr_match = True
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb"))
