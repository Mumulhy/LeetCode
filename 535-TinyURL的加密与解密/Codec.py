# -*- coding: utf-8 -*-
# LeetCode 535-TinyURL的加密与解密

"""
Created on Wed Jun 29 15:00 2022

@author: _Mumu
Environment: py38
"""


class Codec:
    def __init__(self):
        self.database = {}
        self.id = -1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.id += 1
        key = str(self.id)
        self.database[key] = longUrl
        return 'http://tinyurl.com/' + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.database[shortUrl.split('/')[-1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
