class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = nums[0]
        temp = 0
        for i in nums:
            temp += i
            if temp < i:
                temp = i
            if maxsum < temp:
                maxsum = temp
            print(temp)
            print(maxsum)
            print('-----')
        return maxsum



#指针