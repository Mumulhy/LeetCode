# -*- coding: utf-8 -*-
# LeetCode 564-寻找最近的回文数

"""
Created on Wed Mar 2 09:31 2022

@author: _Mumu
Environment: py39
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10 ** (m - 1) - 1, 10 ** m + 1]
        prefix = int(n[:(m + 1) // 2])
        for x in range(prefix - 1, prefix + 2):
            y = x if m & 1 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)
        print(candidates)

        ans = candidates[0]
        num = int(n)
        min_diff = abs(ans - num)
        for candidate in candidates:
            if candidate != num:
                if (now_diff := abs(candidate - num)) < min_diff or (now_diff == min_diff and candidate < ans):
                    ans = candidate
                    min_diff = now_diff
        return str(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.nearestPalindromic('1'))
