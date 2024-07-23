# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def maxDepth(node):
            if not node:
                return 0
        
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            return 1 + max(left, right)

    
        queue = deque([root])
        lenTree = maxDepth(root)
        print(lenTree)
        
        track = 0
        sumtree = 0
        
        while queue:
            current_level = len(queue)
            track += 1
            
            for _ in range(current_level):
                node = queue.popleft()
        
                if track == lenTree:
                    sumtree += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return sumtree
                
    
    
        
                
        
        