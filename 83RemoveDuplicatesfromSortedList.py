# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        
        
        
        while p != None and p.next != None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


#因为是sorted的 linklist 所以不会出现 【1，2，2，1】 且重复的数字只会出现在这个数字之后