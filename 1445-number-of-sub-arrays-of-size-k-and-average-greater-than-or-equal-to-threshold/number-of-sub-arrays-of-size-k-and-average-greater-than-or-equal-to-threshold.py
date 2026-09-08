class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans=0
        n=len(arr)
        s=sum(arr[0:k])
        if (s//k)>=threshold:
            ans=ans+1
        l=0
        r=k
        for i in range(k,n):
            s=s+arr[r]
            s=s-arr[l]
            l=l+1
            r=r+1
            if (s//k)>=threshold:
                ans=ans+1
        return ans

            
        