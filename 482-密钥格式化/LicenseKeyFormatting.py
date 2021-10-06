# -*- coding: utf-8 -*-
# LeetCode 482-密钥格式化

"""
Created on Mon Oct 4 22:53 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')[::-1].upper()
        key = [s[i:i + k] for i in range(0, len(s), k)]
        return '-'.join(key)[::-1]

        # n = len(s) - s.count('-')
        # firstGroup = n % k
        # groupsOfK = n // k
        # i, j, l = 0, 0, 0
        # key = ''
        # while j < firstGroup:
        #     if s[i] == '-':
        #         key += s[l:i].upper()
        #         l = i + 1
        #     else:
        #         j += 1
        #     i += 1
        # if firstGroup:
        #     key += s[l:i].upper()
        #     if groupsOfK:
        #         key += '-'
        #     l = i
        # for m in range(groupsOfK):
        #     j = 0
        #     while j < k:
        #         if s[i] == '-':
        #             key += s[l:i].upper()
        #             l = i + 1
        #         else:
        #             j += 1
        #         i += 1
        #     if m == groupsOfK - 1:
        #         key += s[l:i].upper()
        #         break
        #     key += s[l:i].upper() + '-'
        #     l = i
        # return key


if __name__ == '__main__':
    s = Solution()
    print(s.licenseKeyFormatting("2-5g-3-J", 2))
