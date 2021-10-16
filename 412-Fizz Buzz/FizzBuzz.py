# -*- coding: utf-8 -*-
# LeetCode 412-Fizz Buzz

"""
Created on Wed Oct 13 16:31 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzzList = []
        for i in range(1, n + 1):
            if i % 5 and i % 3:
                fizzBuzzList.append(str(i))
            elif i % 5:
                fizzBuzzList.append('Fizz')
            elif i % 3:
                fizzBuzzList.append('Buzz')
            else:
                fizzBuzzList.append('FizzBuzz')
        return fizzBuzzList


if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))
