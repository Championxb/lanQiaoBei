from typing import List


# 215.数组中的第k个最大元素
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 示例 1:
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5

# 示例 2:
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4

class Solution:
    # 调整
    def heapify(self, arr: List[int], n: int, i: int) -> int:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    # 从最后一个非叶子节点开始，依次进行heapify操作，直到根节点   大根堆
    def create(self, arr: List[int]):
        lenth = len(arr)
        for i in range(int(lenth / 2 - 1), -1, -1):
            self.heapify(arr, lenth, i)
        return arr

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.create(nums)
        lenth = len(nums)
        end = lenth - k - 1
        for i in range(lenth - 1, end, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
        return nums[lenth - k]

s = Solution()
# print(s.findKthLargest([16, 9, 10, 14, 7],2))
print(s.findKthLargest([2,1],2))
