class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        f = -1
        ls =-1

        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                f = mid
                r = mid -1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        l = 0
        r = len(nums) - 1
        while l<= r:
            mid = (l+r)//2
            if target == nums[mid]:
                ls = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [f,ls]

       



                




        