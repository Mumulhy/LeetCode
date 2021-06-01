# 461-汉明距离

Author：_Mumu

创建日期：2021/6/1

通过日期：2021/6/1

![](https://github.com/Mumulhy/LeetCode/blob/master/461-汉明距离/通过截图2.jpg)

![](https://github.com/Mumulhy/LeetCode/blob/master/461-汉明距离/通过截图1.jpg)

*****

踩过的坑：

1. 一遍过，舒服了
2. 因为之前写过异或的题，所以察觉到汉明距离其实就是异或的二进制中的1的个数，但是我却不知道python有`str.count(sub_str)`这样的写法，导致写得有些麻烦，看了大佬的写法才知道，学习了！

已解决：24/2105

*****

难度：简单

问题描述：

两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

 

示例 1：

输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
示例 2：

输入：x = 3, y = 1
输出：1


提示：

0 <= x, y <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance