# 48.旋转图像
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
#
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
# https://leetcode.cn/problems/rotate-image/description/?envType=study-plan-v2&envId=top-100-liked


from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        for i in range(l // 2):  # 旋转圈数
            for j in range((l + 1) // 2):  # 边交换次数
                temp = matrix[i][j]
                matrix[i][j] = matrix[l - 1 - j][i]
                matrix[l - 1 - j][i] = matrix[l - 1 - i][l - 1 - j]
                matrix[l - 1 - i][l - 1 - j] = matrix[j][l - 1 - i]
                matrix[j][l - 1 - i] = temp

                # if (j == 0):
                #     matrix[i][j], matrix[l - i][j] \
                #         = matrix[l - i][j], matrix[i][j]
                #     matrix[i][l - j], matrix[l - i][l - j] \
                #         = matrix[l - i][l - j], matrix[i][l - j]
                #     matrix[l - i][l - j], matrix[i][j] \
                #         = matrix[i][j], matrix[l - i][l - j]
                # else:
                #     matrix[i][j], matrix[j][l - i] = matrix[j][l - i], matrix[i][j]
                #     matrix[0][i - j], matrix[i - j][i] = matrix[i - j][i], matrix[0][i - j]
                #     matrix[i][j], matrix[0][i - j] = matrix[0][i - j], matrix[i][j]
                print(i, j, matrix)


s = Solution()
s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s.rotate([[1, 2], [3, 4]])
