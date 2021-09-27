# -*- coding: utf-8 -*-
# LeetCode 639-解码方法II

"""
Created on Mon Sept 27 14:08 2021

@author: _Mumu
Environment: py38
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        fn_1 = 0
        fn = 1
        last = ''
        for now in s:
            fn_2 = fn_1
            fn_1 = fn
            if now == '*':
                if last == '*':
                    fn = (fn_2 * 15 + fn_1 * 9) % 1000000007
                elif last == '1':
                    fn = (fn_2 * 9 + fn_1 * 9) % 1000000007
                elif last == '2':
                    fn = (fn_2 * 6 + fn_1 * 9) % 1000000007
                else:
                    fn = (fn_1 * 9) % 1000000007
            elif now == '7' or now == '8' or now == '9':
                if last == '*' or last == '1':
                    fn = (fn_2 + fn_1) % 1000000007
                else:
                    fn = fn_1
            elif now == '0':
                if last == '*':
                    fn = (fn_2 * 2) % 1000000007
                elif last == '1' or last == '2':
                    fn = fn_2
                else:
                    return 0
            else:
                if last == '*':
                    fn = (fn_2 * 2 + fn_1) % 1000000007
                elif last == '1' or last == '2':
                    fn = (fn_2 + fn_1) % 1000000007
                else:
                    fn = fn_1
            last = now
        return fn

        # fn_2 = 0
        # fn_1 = 1
        # last = ''
        # for now in s:
        #     fn = 0
        #     if now == '*':
        #         fn += fn_1 * 9
        #     elif now == '0':
        #         pass
        #     else:
        #         fn += fn_1
        #     if last:
        #         if last == '*':
        #             if now == '*':
        #                 fn += fn_2 * 15
        #             elif now >= '7':
        #                 fn += fn_2
        #             else:
        #                 fn += fn_2 * 2
        #         elif last == '1':
        #             if now == '*':
        #                 fn += fn_2 * 9
        #             else:
        #                 fn += fn_2
        #         elif last == '2':
        #             if now == '*':
        #                 fn += fn_2 * 6
        #             elif now >= '7':
        #                 pass
        #             else:
        #                 fn += fn_2
        #         else:
        #             pass
        #     last = now
        #     fn_2 = fn_1
        #     fn_1 = fn
        # return fn % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('130'))
