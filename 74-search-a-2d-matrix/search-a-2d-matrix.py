class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        h = m * n-1
        while l <= h:
            mid = (l + h)//2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] > target:
                h = mid -1
            else:
                l = mid+1
        return False


        
        