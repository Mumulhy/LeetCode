# -*- coding: utf-8 -*-
# LeetCode 661-图片平滑器

"""
Created on Thu Mar 24 09:58 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = [[0] * n for _ in range(m)]
        diff = [-1, 0, 1, 0, 0, -1, 1, 1, -1, -1]
        for i in range(m):
            for j in range(n):
                s = 0
                dev = 0
                for k in range(9):
                    x, y = i + diff[k], j + diff[k + 1]
                    if 0 <= x < m and 0 <= y < n:
                        s += img[x][y]
                        dev += 1
                ans[i][j] = s // dev
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
