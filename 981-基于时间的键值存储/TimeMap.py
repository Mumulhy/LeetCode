# -*- coding: utf-8 -*-
# LeetCode 981-基于时间的键值存储

"""
Created on Sat Jul 10 19:37 2021

@author: _Mumu
Environment: py38
"""


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.info = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.info:
            self.info[key][0].append(timestamp)
            self.info[key][1].append(value)
        else:
            self.info[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.info:
            if timestamp < self.info[key][0][0]:
                return ''
            if timestamp >= self.info[key][0][-1]:
                return self.info[key][1][-1]
            left = 0
            right = len(self.info[key][0])
            while right > left + 1:
                mid = (left + right) // 2
                if self.info[key][0][mid] <= timestamp:
                    left = mid
                else:
                    right = mid
            return self.info[key][1][left]
        else:
            return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == '__main__':
    kv = TimeMap()
    print(kv.set("foo", "bar", 1))
    print(kv.get("foo", 1))
    print(kv.get("foo", 3))
    print(kv.set("foo", "bar2", 4))
    print(kv.get("foo", 4))
    print(kv.get("foo", 5))
