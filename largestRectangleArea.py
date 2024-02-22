# 84. 柱状图中最大的面积给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。


# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10


# 思路："单调栈" 当前的数字可以向两边拓展，遇到比自己大的就接着拓展，小的就停止，
# 然后用自己的高度乘以拓展的宽度，每次都跟新最大面积，时间复杂度同样为O(N^2).

from typing import List


# 细节:
# 栈底要垫上-1，表示栈底。
# 循环结束，要清理堆栈。此时所有栈中继续存放的元素的右边界c都是结尾len(height)-1
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        maxArea = 0
        for i in range(len(heights)):
            while stack and (stack[-1] <= heights[i]):
                height_index = stack.pop()
                maxArea = max(maxArea, heights[height_index] * (i - stack[-1] - 1))
            stack.append(i)
        return maxArea