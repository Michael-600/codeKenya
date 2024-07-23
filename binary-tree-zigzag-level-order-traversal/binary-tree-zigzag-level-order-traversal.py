# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        queue = deque([root])
        left_to_right = True
        ans = []
        
        while queue:
            current_level = len(queue)
            curr_list = deque()
            
            for _ in range(current_level):
                node = queue.popleft()
                
                
                if  left_to_right:
                    curr_list.append(node.val)
                else:
                    curr_list.appendleft(node.val)
                    
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            ans.append(list(curr_list))
            left_to_right = not left_to_right
            
        return ans
                
                
            
            
        