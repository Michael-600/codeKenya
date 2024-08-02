# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None 

        dummy = ListNode(0)
        dummy.next = head
        before = dummy

        for _ in range(left - 1):
            before = before.next


        prev = before
        curr = before.next

        for i in range(left, right + 1):
            nextt = curr.next
            curr.next = prev
            prev = curr 
            curr = nextt

        before.next.next = curr
        before.next = prev

        return dummy.next
            
        
            
            
        
            
        
            
    
        