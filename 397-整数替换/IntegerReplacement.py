# -*- coding: utf-8 -*-
# LeetCode 397-整数替换

"""
Created on Fri Nov 19 11:03 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        step = 0
        while n > 1:
            if n & 1 == 0:
                step += 1
                n >>= 1
            elif n % 4 == 1:
                step += 2
                n >>= 1
            else:
                if n == 3:
                    return step + 2
                else:
                    step += 2
                    n = n // 2 + 1
        return step

        # if n == 1:
        #     return 0
        # if n % 2 == 0:
        #     return 1 + self.integerReplacement(n // 2)
        # return 2 + min(self.integerReplacement(n // 2), self.integerReplacement(n // 2 + 1))

        # step = 0
        # stack = [n]
        # while True:
        #     if 1 in stack:
        #         return step
        #     new_stack = []
        #     for num in stack:
        #         if num & 1 == 1:
        #             new_stack.append(num - 1)
        #             new_stack.append(num + 1)
        #         else:
        #             new_stack.append(num >> 1)
        #     stack = new_stack
        #     step += 1


if __name__ == '__main__':
    s = Solution()
    print(s.integerReplacement(15))
