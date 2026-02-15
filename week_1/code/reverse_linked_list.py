from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        """
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Helper to print list
def printList(head):
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: 1->2->3->4->5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original:")
    printList(head)
    reversed_head = sol.reverseList(head)
    print("Reversed (Expected: 5->4->3->2->1):")
    printList(reversed_head)
