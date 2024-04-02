# 40.组合总和II
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# 说明： 所有数字（包括目标数）都是正整数。解集不能包含重复的组合。


# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# 示例 2:

# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.combination = []
        self.startIndex = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        self.backtracking(candidates, target, self.startIndex)
        return self.result

    def backtracking(self, candidates, target, index):
        if sum(self.combination) == target:
            self.result.append(self.combination[:])
            return
        for i in range(index, len(candidates)):
            if sum(self.combination)+candidates[i] <= target:
                if i > index and candidates[i-1] == candidates[i]:
                    print(candidates[i-1], candidates[i])
                    continue
                else:
                    self.combination.append(candidates[i])
                    self.backtracking(candidates, target, i + 1)
                    self.combination.pop()

candidates = [10,1,2,7,6,1,5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))