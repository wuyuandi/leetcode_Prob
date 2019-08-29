class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if s[-1] == '':
        #     return 0
        # else:
        s = s.strip(' ')
        s = s.split(' ')
        return len(s[-1])
        