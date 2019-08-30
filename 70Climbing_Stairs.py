class Solution:
    def climbStairs(self, n: int) -> int:

        a = 1
        b = 2
        temp = 0
        for _ in range(3,n):
            temp = a+b
            a = b
            b = temp

        
        return a+b if n>2 else n
#DP  F(n) = F(n-1)+F(n-2)