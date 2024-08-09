# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dm = 0
        
        def dfs(node):
            if not node:
                return 0
            
            nonlocal dm 
            left = dfs(node.left)
            right = dfs(node.right)
            
            dm = max(dm, left+right)
            
            return max(left, right) + 1
        
        dfs(root)
        return dm
            
           
        
        