class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)  == 0:
            return 0
            
        mx = 1
        c = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                c+=1
                if c > mx:
                    mx = c
            else:
                c = 1
        return mx
