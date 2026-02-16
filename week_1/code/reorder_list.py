from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        You are given the head of a singly linked-list. The list can be represented as:
        L0 -> L1 -> ... -> Ln - 1 -> Ln
        Reorder the list to be on the following form:
        L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...
        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
        """
        if not head: return
        
        # 1. Find Middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse Second Half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # 3. Merge Two Halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

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
    
    # Test 1: 1->2->3->4
    head1 = createList([1,2,3,4])
    print("Original 1:")
    printList(head1)
    sol.reorderList(head1)
    print("Reordered 1 (Expected: 1->4->2->3):")
    printList(head1)

    # Test 2: 1->2->3->4->5
    head2 = createList([1,2,3,4,5])
    print("Original 2:")
    printList(head2)
    sol.reorderList(head2)
    print("Reordered 2 (Expected: 1->5->2->4->3):")
    printList(head2)
