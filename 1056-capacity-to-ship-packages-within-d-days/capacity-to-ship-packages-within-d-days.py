class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low+high)//2
            load = 0
            ds = 1
            for weight in weights:
                if load+weight > mid:
                    ds += 1
                    load = 0
                load += weight
            if ds <= days:
                high = mid
            else:
                low = mid+1
        return low

  

            


            
             

        