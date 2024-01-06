/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        Set<ListNode> mySet = new HashSet<>();
        ListNode temp = head;

        while ( temp != null){
            if (mySet.contains(temp)){
                return temp;
            }else{
                mySet.add(temp);
                temp = temp.next;

            } 
        }
        
        return null;
        
        
        
    }
}