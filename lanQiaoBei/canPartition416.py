# 416.分割等和子集
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意: 每个数组中的元素不会超过 100 数组的大小不会超过 200
#
# 示例 1:
# 输入: [1, 5, 11, 5]
# 输出: true
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].


# 示例 2:
# 输入: [1, 2, 3, 5]
# 输出: false
# 解释: 数组不能分割成两个元素和相等的子集.

# 提示：
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
from typing import List


# 思路：
# 背包的体积为sum / 2
# 背包要放入的商品（集合里的元素）重量为 元素的数值，价值也为元素的数值
# 背包如果正好装满，说明找到了总和为 sum / 2 的子集。
# 背包中每一个元素是不可重复放入
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        else:
            target = int(sum(nums) / 2)
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums))]

        # 初始第一行---第0个物品的价值
        for i in range(1, target + 1):
            if i >= nums[0]:
                dp[0][i] = nums[0]

        for m in range(1, len(nums)):  # 物品
            for n in range(1, target + 1):  # 背包重量
                if n < nums[m]:  # 放不下当前物品
                    dp[m][n] = dp[m - 1][n]  # dp[m-1][n]为不放当前物品的价值 也就是和前面的价值相同
                else:  # dp[m-1][n-nums[m]]为背包容量为n-nums[m]不放物品m的价值，
                    # dp[m-1][n-nums[m]]+nums[m]则为背包放入m后的价值
                    dp[m][n] = max(dp[m - 1][n], dp[m - 1][n - nums[m]] + nums[m])

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                print(dp[i][j], end='\t')
            print("\n")
        print(dp)
        if dp[-1][target] == target:
            return True
        else:
            return False


nums = [1, 5, 11, 5]
s = Solution()
print(s.canPartition(nums))
