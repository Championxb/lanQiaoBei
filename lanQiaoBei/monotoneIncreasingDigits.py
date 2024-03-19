# 738.单调递增的数字
# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
# 给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

# 示例 1:
# 输入: n = 10
# 输出: 9
#
# 示例 2:
# 输入: n = 1234
# 输出: 1234
#
# 示例 3:
# 输入: n = 332
# 输出: 299


# 思路：从后往前遍历，碰到前一个比后一个大的，前一个就减一，并记录flag为当前需要改变为9的位置为当前位置
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = [int(x) for x in str(n)]
        flag=len(nums)
        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i - 1]:
                nums[i-1], flag = nums[i - 1] - 1, i

        print(nums[:flag],flag)
        nums = nums[:flag]+[9 for n in nums[flag:]]
        return int(''.join(str(n) for n in nums))


n = 100
s = Solution()
print(s.monotoneIncreasingDigits(n))