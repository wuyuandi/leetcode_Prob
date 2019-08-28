class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        #input 'LVIII'
        #Input: "MCMXCIV"
        for i in range(len(s)-1):
            if mapping[s[i]] >= mapping[s[i+1]]:
                result += mapping[s[i]]
            else:
                result -= mapping[s[i]]
        result += mapping[s[-1]]
        
        return result


        