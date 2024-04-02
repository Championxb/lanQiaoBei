# 39. 组合总和
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。

# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。

# 示例 1：
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为： [ [7], [2,2,3] ]

# 示例 2：
# 输入：candidates = [2,3,5], target = 8,
# 所求解集为： [ [2,2,2,2], [2,3,3], [3,5] ]
from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.combination = []
        self.unique_tuples = set()  # 集合
        self.startIndex = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking(candidates, target, self.startIndex)
        # 使用集合来存储子列表的元素，忽略顺序   将子列表中的元素转换为元组是为了确保集合中的元素是可哈希的
        # self.unique_tuples = set(tuple(sorted(sublist)) for sublist in self.result)
        # # print(self.unique_tuples)
        # # 将集合转换为列表
        # self.result = [list(sublist) for sublist in self.unique_tuples]
        return self.result

    def backtracking(self, candidates, target, startIndex):
        if sum(self.combination) == target:
            self.result.append(self.combination[:])
            return
        # if sum(self.combination) > target:
        #     return
        for i in range(startIndex, len(candidates)):
            if sum(self.combination)+candidates[i] <= target:
                self.combination.append(candidates[i])
                self.backtracking(candidates, target,i)
                self.combination.pop()


candidates = [2, 3, 6, 7]
target = 7
s = Solution()
print(s.combinationSum(candidates, target))