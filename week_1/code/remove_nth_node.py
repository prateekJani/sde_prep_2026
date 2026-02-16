from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given the head of a linked list, remove the nth node from the end of the list and return its head.
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next
            
        # Delete the node
        left.next = left.next.next
        
        return dummy.next

# Helper to print list
def printList(head):
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

# Helper to create list
def createList(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: 1->2->3->4->5, n=2
    head1 = createList([1,2,3,4,5])
    print("Original 1:")
    printList(head1)
    new_head1 = sol.removeNthFromEnd(head1, 2)
    print("Removed 2nd from end (Expected: 1->2->3->5):")
    printList(new_head1)

    # Test 2: 1, n=1
    head2 = createList([1])
    print("Original 2:")
    printList(head2)
    new_head2 = sol.removeNthFromEnd(head2, 1)
    print("Removed 1st from end (Expected: Empty):")
    printList(new_head2)

    # Test 3: 1->2, n=1
    head3 = createList([1,2])
    print("Original 3:")
    printList(head3)
    new_head3 = sol.removeNthFromEnd(head3, 1)
    print("Removed 1st from end (Expected: 1):")
    printList(new_head3)
