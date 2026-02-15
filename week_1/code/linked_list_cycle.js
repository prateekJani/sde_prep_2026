/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
function ListNode(val) {
    this.val = val;
    this.next = null;
}

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
    let slow = head;
    let fast = head;

    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow === fast) {
            return true;
        }
    }
    return false;
};

// Helper to create a cycle for testing
function createCycleList(arr, pos) {
    if (!arr.length) return null;
    let head = new ListNode(arr[0]);
    let curr = head;
    let nodes = [head];
    for (let i = 1; i < arr.length; i++) {
        let node = new ListNode(arr[i]);
        curr.next = node;
        curr = node;
        nodes.push(node);
    }

    if (pos !== -1) {
        curr.next = nodes[pos];
    }

    return head;
}

// Test cases
// Test 1: [3,2,0,-4], pos = 1 (Cycle)
let head1 = createCycleList([3, 2, 0, -4], 1);
console.log("Test 1 (Cycle):", hasCycle(head1), "(Expected: true)");

// Test 2: [1,2], pos = 0 (Cycle)
let head2 = createCycleList([1, 2], 0);
console.log("Test 2 (Cycle):", hasCycle(head2), "(Expected: true)");

// Test 3: [1], pos = -1 (No Cycle)
let head3 = createCycleList([1], -1);
console.log("Test 3 (No Cycle):", hasCycle(head3), "(Expected: false)");
