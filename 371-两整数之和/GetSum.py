# -*- coding: utf-8 -*-
# LeetCode 371-两整数之和

"""
Created on Sun Sept 26 22:42 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK1 = 2048
        MASK2 = 1024
        MASK3 = 2047
        a %= MASK1
        b %= MASK1
        while b:
            up = ((a & b) << 1) % MASK1
            a = (a ^ b)
            b = up
        if a & MASK2:
            return ~(a ^ MASK3)
        else:
            return a

    # def getSum(self, a: int, b: int) -> int:
    #     if a == 0:
    #         return b
    #     if b == 0:
    #         return a
    #     if a > 0 and b > 0:
    #         return self.getAdd(a, b, False)
    #     if a < 0 and b < 0:
    #         return self.getAdd(a, b, True)
    #     if a < b:
    #         a, b = b, a
    #     if a >= abs(b):
    #         return self.getMinus(a, abs(b), False)
    #     else:
    #         return self.getMinus(abs(b), a, True)
    #
    # def getAdd(self, a: int, b: int, isMinus: bool) -> int:
    #     if isMinus:
    #         a = bin(a)[3:]
    #         b = bin(b)[3:]
    #     else:
    #         a = bin(a)[2:]
    #         b = bin(b)[2:]
    #     if len(a) < len(b):
    #         a, b = b, a
    #     n = len(a)
    #     b = '{}{}'.format('0' * (n - len(b)), b)
    #     s = ''
    #     up = 0
    #     for i in range(n):
    #         s = '{}{}'.format(s, int(a[n - 1 - i]) ^ int(b[n - 1 - i]) ^ up)
    #         if up:
    #             if a[n - 1 - i] == '1' or b[n - 1 - i] == '1':
    #                 up = 1
    #             else:
    #                 up = 0
    #         else:
    #             if a[n - 1 - i] == '1' and b[n - 1 - i] == '1':
    #                 up = 1
    #             else:
    #                 up = 0
    #     if up == 1:
    #         s = '{}{}'.format(s, 1)
    #     if isMinus:
    #         s = '{}{}'.format(s, '-')
    #     return int(s[::-1], 2)
    #
    # def getMinus(self, a: int, b: int, isMinus: bool) -> int:
    #     if a == b:
    #         return 0
    #     a = bin(a)[2:]
    #     b = bin(b)[2:]
    #     n = len(a)
    #     b = '{}{}'.format('0' * (n - len(b)), b)
    #     s = ''
    #     borrow = 0
    #     for i in range(n):
    #         s = '{}{}'.format(s, int(a[n - 1 - i]) ^ int(b[n - 1 - i]) ^ borrow)
    #         if borrow:
    #             if a[n - 1 - i] == '1' and b[n - 1 - i] == '0':
    #                 borrow = 0
    #             else:
    #                 borrow = 1
    #         else:
    #             if a[n - 1 - i] == '0' and b[n - 1 - i] == '1':
    #                 borrow = 1
    #             else:
    #                 borrow = 0
    #     if isMinus:
    #         s = '{}{}'.format(s, '-')
    #     return int(s[::-1], 2)


if __name__ == '__main__':
    s = Solution()
    print(s.getSum(-16, -15))
