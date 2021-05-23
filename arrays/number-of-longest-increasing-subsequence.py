class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        for j in range(1,len(nums)):
            for i in range(j):
               if nums[j] > nums[i]:
                   arr[j] = arr[i] + 1
        
        return arr.count(max(arr))

        