# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        '''递归'''
        output = []
        self.traverse(root,0,output)
        output.reverse()
        return output
    def traverse(self,root,depth,output):
        if root is None:
            return 
        if depth == len(output):
            output.append([])
        
        self.traverse(root.left, depth+1,output)
        self.traverse(root.right, depth+1,output)
        output[depth].append(root.val)
