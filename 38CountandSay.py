class Solution:
    def countAndSay(self, n: int) -> str:
        if n ==1:
            return "1"
        s= list(self.countAndSay(n-1))
        result=''
        split_s=[]
        while s:
            i=s.pop(0)
            tmp = i
            while(s and s[0]==i):
                tmp +=s.pop(0)
            split_s.append(tmp)
        for one in split_s:
            result += str(len(one))+one[0]
        return result

####***** 递归解