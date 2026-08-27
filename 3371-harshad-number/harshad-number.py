class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        summ = 0
        Num = x
        while x != 0:
            digit = x % 10
            summ  = summ + digit
            x  = x // 10
        if Num % summ == 0:
            return summ
        else:
            return -1
        