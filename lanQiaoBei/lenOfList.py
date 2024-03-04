class Solution:
    def getMaxLen(self, nums):
        maxLen = 0
        sign = 1
        t = 0
        mark = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            for j in range(i, len(nums)):
                if nums[j] != 0 and nums[j] > 0:
                    if sign > 0:
                        mark += 1
                    continue
                if nums[j] != 0 and nums[j] < 0:
                    sign *= -1
                    t += 1
                    if sign > 0:
                        if mark ==0:
                            mark = 2 if t%2 == 0 else 1
                        else:
                            mark = 1 + 2 if t % 2 == 0 else 1 + 1
                        t = 0
                    continue
                if nums[j] == 0:
                    break
            sign = 1
            if mark > maxLen:
                maxLen = mark
                mark = 0
        return maxLen
nums = [1,2,3,5,-6,4,0,10]
re = Solution()
result = re.getMaxLen(nums)
print(result)
