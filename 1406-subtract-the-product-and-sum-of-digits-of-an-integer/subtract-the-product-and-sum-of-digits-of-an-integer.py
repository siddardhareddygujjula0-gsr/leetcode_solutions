class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        product = 1
        sumn = 0
        while n != 0:
            product *= n % 10
            sumn += n%10
            n //= 10
        return product - sumn
        