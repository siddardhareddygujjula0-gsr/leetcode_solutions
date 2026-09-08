class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxl=0
        n=len(nums)
        left=0
        zeroes=0
        for right in range(n):
            if nums[right]==0:
                zeroes+=1
            while zeroes>k:
                if nums[left]==0:
                    zeroes-=1
                left+=1
            maxl=max(maxl,right-left+1)
        return maxl
        
        