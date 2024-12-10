/**
 * Solution for the "Add Two Numbers" problem.
 * Time complexity: O(n), where n is the maximum length of the two linked lists.
 * Space complexity: O(n), due to the new linked list created to store the result.
 * 
 * ListNode class:
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution
{
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        var head = new ListNode();
        var tail = head;
        var carry = 0;

        while (l1 != null || l2 != null || carry != 0)
        {
            var val1 = l1?.val ?? 0;
            var val2 = l2?.val ?? 0;
            var result = val1 + val2 + carry;

            carry = result / 10;
            result = result % 10;

            tail.next = new ListNode(result);
            tail = tail.next;

            l1 = l1?.next ?? null;
            l2 = l2?.next ?? null;
        }

        return head.next;
    }
}