# -*- coding: utf-8 -*-
# LeetCode 420-强密码检验器

"""
Created on Sat Apr 2 09:49 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = has_upper = has_digit = False
        for ch in password:
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
        categories = has_lower + has_upper + has_digit

        if n < 6:
            return max(6 - n, 3 - categories)

        if n <= 20:
            replace = cnt = 0
            curr = '#'
            for ch in password:
                if ch == curr:
                    cnt += 1
                else:
                    replace += cnt // 3
                    curr = ch
                    cnt = 1
            replace += cnt // 3
            return max(replace, 3 - categories)

        replace, remove = 0, n - 20
        rm2 = cnt = 0
        curr = '#'
        for ch in password:
            if ch == curr:
                cnt += 1
            else:
                if remove > 0 and cnt >= 3:
                    if cnt % 3 == 0:
                        remove -= 1
                        replace -= 1
                    elif cnt % 3 == 1:
                        rm2 += 1
                replace += cnt // 3
                cnt = 1
                curr = ch
        if remove > 0 and cnt >= 3:
            if cnt % 3 == 0:
                remove -= 1
                replace -= 1
            elif cnt % 3 == 1:
                rm2 += 1
        replace += cnt // 3
        use2 = min(replace, rm2, remove // 2)
        replace -= use2
        remove -= use2 * 2
        use3 = min(replace, remove // 3)
        replace -= use3
        remove -= use3 * 3
        return (n - 20) + max(replace, 3 - categories)
