# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def backtracking(root):
            if not root:
                return 1
            left = backtracking(root.left)
            if not left:
                return 0
            right = backtracking(root.right)
            if not right:
                return 0
            return max(left,right)+1 if abs(left-right)<=1 else 0
        if not root:
            return True
        return True if backtracking(root) else False