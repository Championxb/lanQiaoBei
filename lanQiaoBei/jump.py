# 45.跳跃游戏II
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
#
# 1) 0 <= j <= nums[i]
# 2) i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。


# 示例 1:
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
# 示例 2:
# 输入: nums = [2,3,0,1,4]
# 输出: 2
from typing import List


# 思路：始终选择能跳最远的位置跳，不断更新最远距离，
# 前一条后面的范围都属于第二跳，在第二跳的范围内找到下一跳的最大范围，更新下一跳的范围和最远距离
class Solution:
    def jump(self, nums: List[int]) -> int:
        step = maxLen = 0
        border = 0  # 当前能跳到最远的的临界位置
        # 之所以不访问最后一个元素，是因为在到达末尾之前，边界值一定大于等于最后一个位置（否则无法到达），
        # 如果等于最后一个元素，就会徒增一步
        for i in range(len(nums) - 1):
            if maxLen >= i:  # 可以不用判断 因为题目说了必然能走到
                maxLen = max(maxLen, i + nums[i])
                if i == border:  # 走到边界时，就更新边界位置，为前一段边界范围内能到达的最远位置
                    border = maxLen
                    step += 1
        return step


nums = [2, 3, 0, 1, 4]
s = Solution()
print(s.jump(nums))
