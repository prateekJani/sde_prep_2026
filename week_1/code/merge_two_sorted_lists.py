from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return it as a sorted list.
        The list should be made by splicing together the nodes of the first two lists.
        """
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next

# Helper to print list
def printList(head):
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

# Helper to create list from array
def createList(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: [1,2,4], [1,3,4]
    l1 = createList([1,2,4])
    l2 = createList([1,3,4])
    print("List 1:")
    printList(l1)
    print("List 2:")
    printList(l2)
    merged = sol.mergeTwoLists(l1, l2)
    print("Merged (Expected: 1->1->2->3->4->4):")
    printList(merged)
