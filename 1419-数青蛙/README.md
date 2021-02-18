# 1419-数青蛙

Author：_Mumu

创建日期：2021/2/18

通过日期：2021/2/18

![](https://github.com/Mumulhy/LeetCode/blob/master/1419-数青蛙/通过截图2.jpg)

![](https://github.com/Mumulhy/LeetCode/blob/master/1419-数青蛙/通过截图1.jpg)

*****

踩过的坑：

1. 第一反应是做一个列表，列表的每个元素是每只青蛙的叫声，但是这样的算法时间复杂度有$O(n^2)$，导致一个长度为$10^5$的测试字符串因为时长无法通过
2. 在题解中找到了时间复杂度为$O(n)$的算法，loop输入的字符串，通过计算当前叫声末尾'c'、'r'、'o'、'a'字符的青蛙个数，则末尾为'k'的个数表示当前空闲（可以叫出下一声'croak'的青蛙）的青蛙个数，于是如果字符串符合规则，loop结束后'k'的个数即为最少所需的青蛙个数

已解决：8/1971

*****

难度：中等

问题描述：

给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 中会混合多个 “croak” 。请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。

注意：要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。

如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。

 

示例 1：

输入：croakOfFrogs = "croakcroak"
输出：1 
解释：一只青蛙 “呱呱” 两次
示例 2：

输入：croakOfFrogs = "crcoakroak"
输出：2 
解释：最少需要两只青蛙，“呱呱” 声用黑体标注
第一只青蛙 "crcoakroak"
第二只青蛙 "crcoakroak"
示例 3：

输入：croakOfFrogs = "croakcrook"
输出：-1
解释：给出的字符串不是 "croak" 的有效组合。
示例 4：

输入：croakOfFrogs = "croakcroa"
输出：-1


提示：

1 <= croakOfFrogs.length <= 10^5
字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking