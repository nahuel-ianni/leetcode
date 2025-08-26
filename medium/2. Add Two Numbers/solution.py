# Solution for the "Add Two Numbers" problem.
# Time complexity: O(n), where n is the maximum length of the two linked lists.
# Space complexity: O(n), due to the new linked list created to store the result.
#
# ListNode class:
#   class ListNode:
#       def __init__(self, val=0, next=None):
#           self.val = val
#           self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy head node to simplify list construction.
        head = ListNode()
        tail = head
        carry = 0

        # Iterate through the linked lists until both are exhausted and no carry remains.
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            result = val1 + val2 + carry
            
            # Update the carry for the next iteration and the result digit for the current node.
            carry, result = divmod(result, 10)

            # Create a new node with the result digit and attach it to the result list.
            tail.next = ListNode(result)
            tail = tail.next

            # Move to the next nodes in the input linked lists, if available.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the next node of the head, which is the start of the result list.
        return head.next
