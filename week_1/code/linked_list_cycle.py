from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
        Return true if there is a cycle in the linked list. Otherwise, return false.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

# Helper to create a cycle for testing
def createCycleList(arr, pos):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    nodes = [head]
    for val in arr[1:]:
        node = ListNode(val)
        curr.next = node
        curr = node
        nodes.append(node)
    
    if pos != -1:
        curr.next = nodes[pos]
    
    return head

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: [3,2,0,-4], pos = 1 (Cycle)
    head1 = createCycleList([3,2,0,-4], 1)
    print(f"Test 1 (Cycle): {sol.hasCycle(head1)} (Expected: True)")
    
    # Test 2: [1,2], pos = 0 (Cycle)
    head2 = createCycleList([1,2], 0)
    print(f"Test 2 (Cycle): {sol.hasCycle(head2)} (Expected: True)")
    
    # Test 3: [1], pos = -1 (No Cycle)
    head3 = createCycleList([1], -1)
    print(f"Test 3 (No Cycle): {sol.hasCycle(head3)} (Expected: False)")
