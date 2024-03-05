# 347.前k个高频元素
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
# 你可以按 任意顺序 返回答案。
from typing import List


# 示例 1:
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]

# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for num in nums:
            if num not in freqDict:
                freqDict[num] = 1
            else:
                freqDict[num] += 1
        # list(freqDict.keys())[list(freqDict.values()).index(2)]  由value查key  把字典列表化
        topK = [n for n in freqDict.values()]
        topK = self.create(topK)  # 堆排序
        lenth = len(topK)
        end = len(topK) - 1 - k

        lastK = []
        # 倒数K个
        for i in range(lenth - 1, end, -1):
            topK[0], topK[i] = topK[i], topK[0]
            k = list(freqDict.keys())[list(freqDict.values()).index(topK[i])]
            del freqDict[k]
            lastK.append(k)
            self.heapify(topK, i, 0)
        return lastK

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

    def create(self, arr: List[int]):
        lenth = len(arr)
        for i in range(int(lenth / 2 - 1), -1, -1):
            self.heapify(arr, lenth, i)
        return arr


nums = [1, 2]
s = Solution()
print(s.topKFrequent(nums, 2))
# st={'a':"'1001" ,'b':'1002','c':'1003','d':'1004'}
# print(list(st.keys())[list(st.values()).index('1004')])
# print(list(st.keys()))
# print(list(st.values()))
# print(list(st.values()).index('1004'))
