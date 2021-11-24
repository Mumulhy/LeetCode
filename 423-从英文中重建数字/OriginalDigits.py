# -*- coding: utf-8 -*-
# LeetCode 423-从英文中重建数字

"""
Created on Wed Nov 24 10:28 2021

@author: _Mumu
Environment: py38
"""

# from collections import defaultdict
from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        counts = Counter(s)
        nums = [0] * 10

        nums[0] = counts['z']
        nums[2] = counts['w']
        nums[4] = counts['u']
        nums[6] = counts['x']
        nums[8] = counts['g']

        nums[1] = counts['o'] - nums[0] - nums[2] - nums[4]
        nums[3] = counts['h'] - nums[8]
        nums[5] = counts['f'] - nums[4]
        nums[7] = counts['s'] - nums[6]

        nums[9] = counts['i'] - nums[6] - nums[8] - nums[5]

        return ''.join(str(i) * nums[i] for i in range(10))

    # def __init__(self):
    #     self._counts = defaultdict(int)
    #     self._nums = [0] * 10
    #
    # def originalDigits(self, s: str) -> str:
    #     '''
    #     zero: z     two: w      four: u     six: x      eight: g
    #     one: o      three: h    five: f     seven: s
    #     nine: e
    #     '''
    #     for letter in s:
    #         self._counts[letter] += 1
    #     self._findZeroByZ()
    #     self._findTwoByW()
    #     self._findFourByU()
    #     self._findSixByX()
    #     self._findEightByG()
    #     self._findOneByO()
    #     self._findThreeByH()
    #     self._findFiveByF()
    #     self._findSevenByS()
    #     self._findNineByE()
    #     return ''.join(str(i) * self._nums[i] for i in range(10))
    #
    # def _findZeroByZ(self) -> None:
    #     self._nums[0] = self._counts['z']
    #     for letter in 'zero':
    #         self._counts[letter] -= self._nums[0]
    #
    # def _findTwoByW(self) -> None:
    #     self._nums[2] = self._counts['w']
    #     for letter in 'two':
    #         self._counts[letter] -= self._nums[2]
    #
    # def _findFourByU(self) -> None:
    #     self._nums[4] = self._counts['u']
    #     for letter in 'four':
    #         self._counts[letter] -= self._nums[4]
    #
    # def _findSixByX(self) -> None:
    #     self._nums[6] = self._counts['x']
    #     for letter in 'six':
    #         self._counts[letter] -= self._nums[6]
    #
    # def _findEightByG(self) -> None:
    #     self._nums[8] = self._counts['g']
    #     for letter in 'eight':
    #         self._counts[letter] -= self._nums[8]
    #
    # def _findOneByO(self) -> None:
    #     self._nums[1] = self._counts['o']
    #     for letter in 'one':
    #         self._counts[letter] -= self._nums[1]
    #
    # def _findThreeByH(self) -> None:
    #     self._nums[3] = self._counts['h']
    #     for letter in 'three':
    #         self._counts[letter] -= self._nums[3]
    #
    # def _findFiveByF(self) -> None:
    #     self._nums[5] = self._counts['f']
    #     for letter in 'five':
    #         self._counts[letter] -= self._nums[5]
    #
    # def _findSevenByS(self) -> None:
    #     self._nums[7] = self._counts['s']
    #     for letter in 'seven':
    #         self._counts[letter] -= self._nums[7]
    #
    # def _findNineByE(self) -> None:
    #     self._nums[9] = self._counts['e']
    #     self._counts.clear()


if __name__ == '__main__':
    s = Solution()
    print(s.originalDigits("fviefuro"))
