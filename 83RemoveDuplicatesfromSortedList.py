class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0,n):
            nums1[i+m] = nums2[i]
        nums1.sort()
#把数组2的数直接放到数组1里，然后sort（）