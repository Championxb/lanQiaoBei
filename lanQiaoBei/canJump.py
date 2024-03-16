# 55.跳跃游戏
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。


# 示例1：
# 输入：nums = [2, 3, 1, 1, 4]
# 输出：true
# 解释：可以先跳1步，从下标0到达下标1, 然后再从下标1跳3步到达最后一个下标。
#
# 示例2：
# 输入：nums = [3, 2, 1, 0, 4]
# 输出：false
# 解释：无论怎样，总会到达下标为3的位置。但该下标的最大跳跃长度是0 ， 所以永远不可能到达最后一个下标。

from typing import List


# 思路：如果当前位置数字是x，就说明当前位置的后面的x个位置都可以到达，以此来记录最远距离
# 一步一步走，并不断更新每个位置能到达位置来更新最远距离，
# 如果走到的位置已经大于最远距离，也就是前面没有路再向前延伸了且没到达最后的位置，就是false
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxLen = 0
        for i in range(len(nums)):
            if maxLen < i:
                return False
            if nums[i] >= len(nums):
                return True
            maxLen = max(maxLen, i + nums[i])

        return True


nums = [3, 2, 1, 0, 4]
s = Solution()
print(s.canJump(nums))
