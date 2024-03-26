# 17.电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.str = ''
        self.index = 0

    def digit_to_letters(self, digit):
        mapping = {
            '#': [],
            '0': [],
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        return mapping.get(digit, [])

    def letterCombinations(self, digits: str) -> List[str]:
        strNums = list(digits)
        digitsList = [self.digit_to_letters(i) for i in strNums]  # 把对应数字的列表传过去
        # print(digitsList)
        self.backtracking(digitsList, self.index)
        return self.result

    def backtracking(self, digitsList, index):
        if len(self.str) == len(digitsList):
            if digitsList:  # 如果不是digitsList是空的 也就是传入的digits不是空
                self.result.append(self.str)
            return
        for i in range(len(digitsList[index])):
            self.str += digitsList[index][i]  # 得到当前递归数字对应列表的字母
            self.backtracking(digitsList, index + 1)
            self.str = self.str[:-1]   # （切片）删除最后一个字母


digits = ""
s = Solution()
print(s.letterCombinations(digits))
