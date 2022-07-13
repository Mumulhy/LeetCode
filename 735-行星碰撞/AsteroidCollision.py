# -*- coding: utf-8 -*-
# LeetCode 735-行星碰撞

"""
Created on Wed Jul 13 09:51 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        n = len(asteroids)
        i = 0
        while i < n and asteroids[i] < 0:
            ans.append(asteroids[i])
            i += 1
        if i == n:
            return ans
        to_collide = []
        for asteroid in asteroids[i:]:
            if asteroid > 0:
                to_collide.append(asteroid)
            elif not to_collide:
                ans.append(asteroid)
            else:
                while to_collide and to_collide[-1] < abs(asteroid):
                    to_collide.pop()
                if not to_collide:
                    ans.append(asteroid)
                    continue
                if to_collide[-1] == abs(asteroid):
                    to_collide.pop()
        return ans + to_collide


if __name__ == '__main__':
    s = Solution()
    print(s.asteroidCollision([-2, -1, 1, 2]))
