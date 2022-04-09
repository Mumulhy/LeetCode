# -*- coding: utf-8 -*-
# LeetCode 780-到达终点

"""
Created on Sat Apr 9 11:59 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx != ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if sx == tx and sy == ty:
            return True
        if sx == tx:
            return ty > sy and (ty - sy) % tx == 0
        if sy == ty:
            return tx > sx and (tx - sx) % ty == 0
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.reachingPoints(sx=1, sy=1, tx=3, ty=5))
