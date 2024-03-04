# 给你一个整数数组 bloomDay，以及两个整数 m 和 k 。
#
# 现需要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。
#
# 花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 时盛开，恰好 可以用于 一束 花中。
#
# 请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。

# 思路是 : 二分法


# 输入：bloomDay = [1,10,3,10,2], m = 3, k = 1
# 输出：3
# 解释：让我们一起观察这三天的花开过程，x 表示花开，而 _ 表示花还未开。
# 现在需要制作 3 束花，每束只需要 1 朵。
# 1 天后：[x, _, _, _, _]   // 只能制作 1 束花
# 2 天后：[x, _, _, _, x]   // 只能制作 2 束花
# 3 天后：[x, _, x, _, x]   // 可以制作 3 束花，答案为 3
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k >len(bloomDay):
            return -1
        # 二分查找
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            # mid作为最小天数，看是否能制作出m束花
            mid = (left + right)//2
            if self.canMake(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid + 1
        return left


    #day为最小天数，看是否能制作出m束花
    def canMake(self, bloomDay: List[int], m: int, k: int, day: int) -> bool:
        flowers = 0
        bouquets = 0
        canDo = False
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    # 重新计数
                    flowers = 0
            else:
                # 花不连续了
                flowers = 0
            if bouquets == m:
                canDo = True
                break
        return canDo
