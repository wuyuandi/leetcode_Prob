class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        i,result = 0, [1]
        while i < rowIndex:
            result = [1] + [result[x]+result[x+1] for x in range(len(result)-1)] + [1]
            i+=1
        return result