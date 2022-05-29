# -*- coding: utf-8 -*-
# LeetCode 468-验证IP地址

"""
Created on Sun May 29 10:22 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP and ':' in queryIP:
            return 'Neither'
        return 'IPv4' if self.validIPv4(queryIP) else 'IPv6' if self.validIPv6(queryIP) else 'Neither'

    def validIPv4(self, IP: str) -> bool:
        sp = IP.split('.')
        if len(sp) != 4:
            return False
        for s in sp:
            if not s or len(s) > 3:
                return False
            if len(s) > 1 and s[0] == '0':
                return False
            if not s.isdigit():
                return False
            if int(s) < 0 or int(s) > 255:
                return False
        return True

    def validIPv6(self, IP: str) -> bool:
        sp = IP.split(':')
        if len(sp) != 8:
            return False
        for s in sp:
            if not s or len(s) > 4:
                return False
            if not s.isdigit():
                for ch in s:
                    if not ch.isdigit() and ch not in 'abcdefABCDEF':
                        return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validIPAddress("192.168.1.0"))
