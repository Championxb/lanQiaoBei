# 84.柱形图中最大的矩形面积
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
from typing import List


# 单调栈，碰到比自己大的就继续扩展栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        maxArea = 0
        for i in range(len(heights)):
            while stack and (heights[stack[-1]] > heights[i]):
                height_index = stack.pop()
                maxArea = max(maxArea, heights[height_index] * (i - stack[-1] - 1))
            stack.append(i)
        return maxArea
