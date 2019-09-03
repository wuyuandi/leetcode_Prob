# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def comparsion(p,q):
            if p and q and p.val == q.val:
                return comparsion(p.left,q.right) and comparsion(p.right,q.left)
            if not p:
                return not q
            return False
            
        return comparsion(root.left,root.right)
        