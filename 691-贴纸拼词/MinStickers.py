# -*- coding: utf-8 -*-
# LeetCode 691-贴纸拼词

"""
Created on Sat May 14 10:26 2022

@author: _Mumu
Environment: py38
"""

from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickers = [Counter(sticker) for sticker in stickers]

        @lru_cache(None)
        def dfs(target: str) -> int:
            if not target:
                return 0
            ans = float('inf')
            for sticker in stickers:
                if target[0] not in sticker:
                    continue
                replaced = rep(sticker, target)
                ans = min(ans, dfs(replaced) + 1)
            return ans

        def rep(sticker: Counter, word: str) -> str:
            for ch in sticker:
                word = word.replace(ch, '', sticker[ch])
            return word

        ans = dfs(target)
        return ans if ans != float('inf') else -1

        # m = len(target)
        #
        # @lru_cache(None)
        # def dp(mask: int) -> int:
        #     if mask == 0:
        #         return 0
        #     res = m + 1
        #     for sticker in stickers:
        #         left = mask
        #         cnt = Counter(sticker)
        #         for i, c in enumerate(target):
        #             if mask >> i & 1 and cnt[c]:
        #                 cnt[c] -= 1
        #                 left ^= 1 << i
        #         if left < mask:
        #             res = min(res, dp(left) + 1)
        #     return res
        #
        # res = dp((1 << m) - 1)
        # return res if res <= m else -1


if __name__ == '__main__':
    s = Solution()
    print(s.minStickers(stickers=["with", "example", "science"], target="thehat"))
