class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            mx = max(nums)
            if mx == nums[i]:
                return i
     

        