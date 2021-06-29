# 168-Excel表列名称

Author：_Mumu

创建日期：2021/6/29

通过日期：2021/6/29

![](https://github.com/Mumulhy/LeetCode/blob/master/168-Excel表列名称/通过截图2.jpg)

![](https://github.com/Mumulhy/LeetCode/blob/master/168-Excel表列名称/通过截图1.jpg)

*****

踩过的坑：

1. 并不完全是26进制呀，也不是27进制，没有另外手算，当然会做错啦

已解决：28/2141

*****

难度：简单

问题描述：

给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...


示例 1：

输入：columnNumber = 1
输出："A"
示例 2：

输入：columnNumber = 28
输出："AB"
示例 3：

输入：columnNumber = 701
输出："ZY"
示例 4：

输入：columnNumber = 2147483647
输出："FXSHRXW"


提示：

1 <= columnNumber <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title