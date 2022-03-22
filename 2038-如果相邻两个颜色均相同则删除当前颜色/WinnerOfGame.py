# -*- coding: utf-8 -*-
# LeetCode 2038-如果相邻两个颜色均相同则删除当前颜色

"""
Created on Tues Mar 22 10:14 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnt = {'A': 0, 'B': 0}
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                cnt[colors[i]] += 1
        return cnt['A'] > cnt['B']


if __name__ == '__main__':
    s = Solution()
    print(s.winnerOfGame("ABBBBBBBAAA"))
