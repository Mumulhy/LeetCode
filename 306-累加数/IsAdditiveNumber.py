# -*- coding: utf-8 -*-
# LeetCode 306-累加数

"""
Created on Mon Jan 10 09:36 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def __init__(self):
        self.num = ''
        self.n = 0

    def isAdditiveNumber(self, num: str) -> bool:
        if (n := len(num)) < 3:
            return False
        self.num = num
        self.n = n
        for second_start in range(1, n - 1):
            if num[0] == '0' and second_start != 1:
                break
            for second_end in range(second_start, n - 1):
                if num[second_start] == '0' and second_end != second_start:
                    break
                if self.valid(second_start, second_end):
                    return True
        return False

    def valid(self, second_start: int, second_end: int) -> bool:
        first_start, first_end = 0, second_start - 1
        while second_end <= self.n - 1:
            third = self.stringAdd(first_start, first_end, second_start, second_end)
            third_start = second_end + 1
            third_end = second_end + len(third)
            if third_end >= self.n or self.num[third_start:third_end + 1] != third:
                break
            if third_end == self.n - 1:
                return True
            first_start, first_end = second_start, second_end
            second_start, second_end = third_start, third_end
        return False

    def stringAdd(self, first_start: int, first_end: int, second_start: int, second_end: int) -> str:
        third = []
        carry, curr = 0, 0
        while first_end >= first_start or second_end >= second_start or carry != 0:
            curr = carry
            if first_end >= first_start:
                curr += ord(self.num[first_end]) - ord('0')
                first_end -= 1
            if second_end >= second_start:
                curr += ord(self.num[second_end]) - ord('0')
                second_end -= 1
            carry = curr // 10
            curr %= 10
            third.append(chr(curr + ord('0')))
        return ''.join(third[::-1])

    # def __init__(self):
    #     self.num = ''
    #     self.n = 0
    #
    # def isAdditiveNumber(self, num: str) -> bool:
    #     if (n := len(num)) < 3:
    #         return False
    #     self.num = num
    #     self.n = n
    #     return self.check()
    #
    # def check(self, start: int = 0, first: int = 0, second: int = 0, first_num: int = 0, second_num: int = 0) -> bool:
    #     if start != 0:
    #         s = start + first
    #         t = start + first + second
    #         if t == self.n:
    #             return True
    #         if self.num[t] == '0':
    #             if first_num + second_num != 0:
    #                 return False
    #         sum2 = first_num + second_num
    #         third = t + max(first, second)
    #         third_num = int(self.num[t:third])
    #         while third_num < sum2 and third < self.n:
    #             third_num = third_num * 10 + int(self.num[third])
    #             third += 1
    #         if third_num == sum2:
    #             third -= t
    #             return self.check(s, second, third, second_num, third_num)
    #         return False
    #     first_num = int(self.num[0])
    #     for first in range(1, self.n // 2 + 1):
    #         if first_num == 0 and first > 1:
    #             break
    #         s = first
    #         second_num = int(self.num[s])
    #         for second in range(1, (self.n - first) // 2 + 1):
    #             if second_num == 0 and second > 1:
    #                 break
    #             t = s + second
    #             if self.num[t] == '0':
    #                 if first_num + second_num != 0:
    #                     second_num *= 10
    #                     continue
    #             sum2 = first_num + second_num
    #             third = t + max(first, second)
    #             third_num = int(self.num[t:third])
    #             while third_num < sum2 and third < self.n:
    #                 third_num = third_num * 10 + int(self.num[third])
    #                 third += 1
    #             if third_num == sum2:
    #                 third -= t
    #                 if self.check(s, second, third, second_num, third_num):
    #                     return True
    #             second_num = second_num * 10 + int(self.num[t])
    #         first_num = first_num * 10 + int(self.num[s])
    #     return False


if __name__ == '__main__':
    s = Solution()
    print(s.isAdditiveNumber('199111992'))
