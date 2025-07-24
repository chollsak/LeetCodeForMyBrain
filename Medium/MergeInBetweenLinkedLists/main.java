/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int counter = 0;

        while(list1 != null) {
            if(counter < a || counter > b) {
                current.next = list1;
                current = current.next;
            }else if(counter == b){
                while(list2 != null){
                    current.next = list2;
                    current = current.next;
                    list2 = list2.next;
                }
            }
            list1 = list1.next;
            counter++;
        }

        return dummy.next;

    }
}