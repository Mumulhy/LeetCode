# -*- coding: utf-8 -*-
# LeetCode 1694-重新格式化电话号码

"""
Created on Sat Oct 1 22:42 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        only_number = ''
        for num in number:
            if num not in ' -':
                only_number += num
        n = len(only_number)
        if n <= 3:
            return only_number
        m = n // 3 if (n % 3) & 1 == 0 else n // 3 - 1
        new_number = [only_number[3 * i:3 * i + 3] for i in range(m)]
        if n % 3 == 2:
            new_number.append(only_number[-2:])
        elif n % 3 == 1:
            new_number.extend([only_number[-4:-2], only_number[-2:]])
        return '-'.join(new_number)


if __name__ == '__main__':
    s = Solution()
    print(s.reformatNumber("--17-5 229 35-39475 "))
