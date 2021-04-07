# 81-搜索旋转排序数组II

Author：_Mumu

创建日期：2021/4/7

通过日期：2021/4/8

![](https://github.com/Mumulhy/LeetCode/blob/master/81-搜索旋转排序数组II/通过截图2.jpg)

![](https://github.com/Mumulhy/LeetCode/blob/master/81-搜索旋转排序数组II/通过截图1.jpg)

*****

踩过的坑：

1. 第一眼没明白题目啥意思，看了评论才知道是写二分法
2. 然后用了很奇怪的写法，写错了，看了解答才知道可以直接用左右端点下标表示区间/(ㄒoㄒ)/~~

已解决：15/1982

*****

难度：中等

问题描述：

已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

 

示例 1：

输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
示例 2：

输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false


提示：

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii