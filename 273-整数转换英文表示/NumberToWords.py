# -*- coding: utf-8 -*-
# LeetCode 273-整数转换英文表示

"""
Created on Mon Oct 11 19:28 2021

@author: _Mumu
Environment: py38
"""

num2Eng = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
           10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
           16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
           30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        return ' '.join(self.findBillions(num))

    def findTens(self, num: int) -> list:
        if num == 0:
            return []
        ones = num % 10
        if num <= 20 or ones == 0:
            return [num2Eng[num]]
        return [num2Eng[num - ones], num2Eng[ones]]

    def findHundreds(self, num: int) -> list:
        if num == 0:
            return []
        if num < 100:
            return self.findTens(num)
        hundreds = num // 100
        tens = num % 100
        return [num2Eng[hundreds], 'Hundred'] + self.findTens(tens)

    def findThousands(self, num: int) -> list:
        if num == 0:
            return []
        if num < 1000:
            return self.findHundreds(num)
        thousands = num // 1000
        hundreds = num % 1000
        return self.findHundreds(thousands) + ['Thousand'] + self.findHundreds(hundreds)

    def findMillions(self, num: int) -> list:
        if num == 0:
            return []
        if num < 1000000:
            return self.findThousands(num)
        millions = num // 1000000
        thousands = num % 1000000
        return self.findHundreds(millions) + ['Million'] + self.findThousands(thousands)

    def findBillions(self, num: int) -> list:
        if num < 1000000000:
            return self.findMillions(num)
        billions = num // 1000000000
        millions = num % 1000000000
        return [num2Eng[billions], 'Billion'] + self.findMillions(millions)


if __name__ == '__main__':
    s = Solution()
    print(s.numberToWords(2126587031))
