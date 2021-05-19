# 1734-解码异或后的排列

Author：_Mumu

创建日期：2021/5/11

通过日期：2021/5/11

![](https://github.com/Mumulhy/LeetCode/blob/master/1734-解码异或后的排列/通过截图2.jpg)

![](https://github.com/Mumulhy/LeetCode/blob/master/1734-解码异或后的排列/通过截图1.jpg)

*****

踩过的坑：

1. 本题的关键是确定perm的第一个数字是什么，因为知道第一个数后，根据异或的性质，可以从第一个数顺次推出剩余的数字；
2. 最开始的时候选择用遍历的方法选择第一个数，这样就导致算法包含了嵌套的循环，时间复杂度就是$O(n^2)$，导致时间太长没法通过；
3. 然后考虑使用异或的性质直接确定第一个数：
   ①前$n$个（$n$为奇数）正整数异或的结果总是0或1，且当$n\equiv1(mod 4)$时，值为0，当$n\equiv3(mod 4)$时，值为1；
   ②encoded列表index为1的项开始隔项遍历做异或可以得到除了perm的第一个数字之外的所有数字异或值；
   ③把①和②得到的两个值取异或就得到了perm的第一个数字；
4. 这个算法的时间复杂度是$O(n)$。

已解决：21/2079

*****

难度：中等

问题描述：

给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。

它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。

给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。

 

示例 1：

输入：encoded = [3,1]
输出：[1,2,3]
解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
示例 2：

输入：encoded = [6,5,4,6]
输出：[2,4,1,5,3]


提示：

3 <= n < 105
n 是奇数。
encoded.length == n - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-xored-permutation