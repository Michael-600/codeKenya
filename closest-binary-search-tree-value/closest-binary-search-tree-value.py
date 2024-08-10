# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node, minSoFar):
            if not node:
                return
                
           
            if abs(target - node.val) < abs(target - minSoFar[0]):
                minSoFar[0] = node.val
            
            if abs(target - node.val) == abs(target - minSoFar[0]):
                 minSoFar[0] = min(node.val, minSoFar[0])
               

            
            if target < node.val:
                dfs(node.left, minSoFar)
            else:
                dfs(node.right, minSoFar)
                

        minn = [root.val]
        dfs(root, minn)
        return minn[0]
                
        
            
            
        
        
        