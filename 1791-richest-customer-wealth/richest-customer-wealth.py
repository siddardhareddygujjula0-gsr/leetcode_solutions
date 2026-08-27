class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0
        for x in accounts:
            if sum(x) > maxwealth:
                maxwealth = sum(x)
        return maxwealth
        