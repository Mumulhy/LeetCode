# -*- coding: utf-8 -*-
# LeetCode 1734-解码异或后的排列

"""
Created on Fri May 11 17:13 2021

@author: _Mumu
Environment: py38
"""

class Solution:
    def decode(self, encoded: list) -> list:
        n = len(encoded) + 1
        if n % 4 == 1:
            xor_all = 1
        else:
            xor_all = 0
        first_num = xor_all
        for i in range((n-1)//2):
            first_num ^= encoded[2*i+1]
        decoded = [first_num]
        for i in encoded:
            decoded.append(decoded[-1]^i)
        return decoded

        # 之前写的愚蠢硬解算法
        # decoded = []
        # n = len(encoded) + 1
        # for i in range(1, n+1):
        #     decoded.append(i)
        #     now = i
        #     for xor in encoded:
        #         now ^= xor
        #         if now in decoded or now > n or now < 1:
        #             break
        #         else:
        #             decoded.append(now)
        #     if len(decoded) == n:
        #         return decoded
        #     else:
        #         decoded.clear()

if __name__ == '__main__':
    s = Solution()
    print(s.decode([6,5,4,6]))