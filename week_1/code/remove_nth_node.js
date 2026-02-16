/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
    let dummy = new ListNode(0, head);
    let left = dummy;
    let right = head;

    while (n > 0 && right) {
        right = right.next;
        n -= 1;
    }

    while (right) {
        left = left.next;
        right = right.next;
    }

    // Delete the node
    left.next = left.next.next;

    return dummy.next;
};

// Helper to print list
function printList(head) {
    let vals = [];
    let curr = head;
    while (curr) {
        vals.push(curr.val);
        curr = curr.next;
    }
    console.log(vals.join(" -> "));
}

// Helper to create list
function createList(arr) {
    if (!arr.length) return null;
    let head = new ListNode(arr[0]);
    let curr = head;
    for (let i = 1; i < arr.length; i++) {
        curr.next = new ListNode(arr[i]);
        curr = curr.next;
    }
    return head;
}

// Test cases
// Test 1: 1->2->3->4->5, n=2
let head1 = createList([1, 2, 3, 4, 5]);
console.log("Original 1:");
printList(head1);
let newHead1 = removeNthFromEnd(head1, 2);
console.log("Removed 2nd from end (Expected: 1->2->3->5):");
printList(newHead1);

// Test 2: 1, n=1
let head2 = createList([1]);
console.log("Original 2:");
printList(head2);
let newHead2 = removeNthFromEnd(head2, 1);
console.log("Removed 1st from end (Expected: Empty):");
printList(newHead2);

// Test 3: 1->2, n=1
let head3 = createList([1, 2]);
console.log("Original 3:");
printList(head3);
let newHead3 = removeNthFromEnd(head3, 1);
console.log("Removed 1st from end (Expected: 1):");
printList(newHead3);
