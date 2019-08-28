class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = 0
        for i in nums:
            if nums[flag] != i:
                flag += 1
                nums[flag] = i
                
        return len(nums) and flag +1
       