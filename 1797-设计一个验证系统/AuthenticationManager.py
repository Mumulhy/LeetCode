# -*- coding: utf-8 -*-
# LeetCode 1797-设计一个验证系统

"""
Created on Thu Apr 8 15:33 2021

@author: _Mumu
Environment: py37
"""


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenIds = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenIds[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenIds and self.tokenIds[tokenId] + self.timeToLive > currentTime:
            self.tokenIds[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        unexpiredTokens = 0
        for item in self.tokenIds:
            if self.tokenIds[item] + self.timeToLive > currentTime:
                unexpiredTokens += 1
        return unexpiredTokens

    # 大佬的这个写法好聪明哦
    # def countUnexpiredTokens(self, currentTime: int) -> int:
    #     limit = currentTime - self.ttl
    #     return sum(x > limit for x in self.token.values())

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
