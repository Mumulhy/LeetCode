# 137-只出现一次的数字II

Author：_Mumu

创建日期：2021/4/30

通过日期：2021/4/30

![](https://github.com/Mumulhy/LeetCode/blob/master/137-只出现一次的数字II/通过截图2.jpg)

![](https://github.com/Mumulhy/LeetCode/blob/master/137-只出现一次的数字II/通过截图1.jpg)

*****

踩过的坑：

1. 很简单但是奇妙解法很多的题，自己是中规中矩计数一遍过
2. 看了占用内存最低以及时间最快的代码，大佬们牛逼

已解决：20/2064

*****

难度：中等

问题描述：

给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

 

示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,99]
输出：99


提示：

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次


进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii