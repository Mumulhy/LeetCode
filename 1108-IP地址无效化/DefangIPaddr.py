# -*- coding: utf-8 -*-
# LeetCode 1108-IP地址无效化

"""
Created on Tues Jun 21 14:42 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == '__main__':
    s = Solution()
    print(s.defangIPaddr(address="1.1.1.1"))
