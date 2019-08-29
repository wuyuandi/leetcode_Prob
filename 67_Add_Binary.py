class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = int(a,2), int(b,2)
        ans = bin(a+b)
        ans = str(ans)
        ans = ans[2:]
        return ans