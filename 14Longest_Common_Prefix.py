class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        print(s1)

        for i,x in enumerate(s1):
            print(i,x)
            if x != s2[i]:
                return s2[:i]
        return s1