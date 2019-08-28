class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # type: str
        index = 0
        if needle in haystack:
            index = haystack.index(needle)
            return index
        else:
            index = -1
            return index