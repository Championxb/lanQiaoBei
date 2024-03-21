# 63.不同的路径II
# 一个机器人位于一个 mxn
# 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1和0来表示。
from typing import List


# 示例 1：
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# |_S_|___|___|
# |___|_X_|___|
# |___|___|_F_|

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:#如果第一个就是障碍物，直接返回0 没有可达路径
            return 0
        # 初始化数组，如果障碍就在边上，则障碍后面或者下面的路径条数都为0
        for i in range(cols):
            if obstacleGrid[0][i] == 1:
                # obstacleGrid[0][i] = 0
                obstacleGrid[0] = obstacleGrid[0][0:i]+[0]*(cols-i)
                break
            else:
                obstacleGrid[0][i] = 1
        print(obstacleGrid)

        for j in range(1, rows):  # 这里排除第0列，因为0列第一个值已经被赋值为1，被转化为了路径条数数组
            if obstacleGrid[j][0] == 1:
                # obstacleGrid[j][0] = 0
                # obstacleGrid[0] = obstacleGrid[0:j][0] + [0] * (rows - j)
                for row in obstacleGrid[j:]:
                    row[0] = 0
                break
            else:
                obstacleGrid[j][0] = 1

        print(obstacleGrid)
        for m in range(1,rows):
            for n in range(1,cols):
                if (m!=0 and n!=0) and obstacleGrid[m][n]==1:
                    obstacleGrid[m][n] = 0  #说明是障碍 
                    continue
                obstacleGrid[m][n] = obstacleGrid[m-1][n] + obstacleGrid[m][n-1]
                print(obstacleGrid)

        return obstacleGrid[-1][-1]

obstacleGrid =[[1],[0]]
# obstacleGrid[0] = [1]*(i+1 for i,v in enumerate(obstacleGrid[0])   )
s = Solution()
print(s.uniquePathsWithObstacles(obstacleGrid))

# a=[[1,2,3,4,5],[6,7,8,9,10],[10,11,12,13,14],[15,16,17,18,19]]
# for row in a[1:]:
#     row[0] = 0
# print(a)

