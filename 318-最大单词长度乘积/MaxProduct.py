# -*- coding: utf-8 -*-
# LeetCode 318-最大单词长度乘积

"""
Created on Wed Nov 17 14:28 2021

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from functools import reduce
from itertools import product
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_masks = defaultdict(int)
        for word in words:
            curr_mask = reduce(lambda x, y: x | (1 << (ord(y) - ord('a'))), word, 0)
            words_masks[curr_mask] = max(words_masks[curr_mask], len(word))
        return max((words_masks[x] * words_masks[y] for x, y in product(words_masks, repeat=2) if x & y == 0),
                   default=0)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct(["a", "aa", "aaa", "aaaa"]))
