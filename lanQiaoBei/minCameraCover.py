from idlelib.tree import TreeNode
from typing import Optional, List


# 968.监控二叉树
# 给定一个二叉树，我们在树的节点上安装摄像头。
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
# 计算监控树的所有节点所需的最小摄像头数量。

# 示例1
#            ()
#            /
#          (X)
#         /   \
#       ()    ()
# 输入：[0,0,null,0,0]
# 输出：1
# 解释：如图所示，一台摄像头足以监控所有节点。

# 示例2
#               ()
#               /
#             (x)
#             /
#            ()
#           /
#         (x)
#            \
#             ()
# 输入：[0,0,null,0,null,0,null,null,0]
# 输出：2
# 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 思路：从低到上，先给叶子节点父节点放个摄像头，然后隔两个节点放一个摄像头，直至到二叉树头结点。

# 用三个数字来表示：
# 0：该节点无覆盖
# 1：本节点有摄像头
# 2：本节点有覆盖

# 情况1：左右节点都有覆盖，此时父节点应该就是无覆盖的状态了
# 情况2：左右节点至少有一个无覆盖的情况，（父节点）应该放摄像头
# 情况3：左右节点至少有一个有摄像头，父节点就应该是2（覆盖的状态）
# 情况4：头结点没有覆盖
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 定义递归函数
        result = [0]  # 用于记录摄像头的安装数量
        if self.traversal(root, result) == 0: # 情况4:父节点没有覆盖
            result[0] += 1

        return result[0]

    def traversal(self, cur: TreeNode, result: List[int]) -> int:
        if not cur:  # 空节点，该节点有覆盖
            return 2

        # 后序遍历
        left = self.traversal(cur.left, result)
        right = self.traversal(cur.right, result)

        # 情况1: 左右节点都有覆盖，则父节点没有覆盖
        if left == 2 and right == 2:
            return 0

        # 情况2:父节点应该放摄像机
        # left == 0 && right == 0 左右节点无覆盖
        # left == 1 && right == 0 左节点有摄像头，右节点无覆盖
        # left == 0 && right == 1 左节点无覆盖，右节点有摄像头
        # left == 0 && right == 2 左节点无覆盖，右节点覆盖
        # left == 2 && right == 0 左节点覆盖，右节点无覆盖
        if left == 0 or right == 0:
            result[0] += 1
            return 1

        # 情况3: 父节点覆盖
        # left == 1 && right == 2 左节点有摄像头，右节点有覆盖
        # left == 2 && right == 1 左节点有覆盖，右节点有摄像头
        # left == 1 && right == 1 左右节点都有摄像头
        if left == 1 or right == 1:
            return 2
