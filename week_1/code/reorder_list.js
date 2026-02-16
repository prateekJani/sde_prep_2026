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
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
    if (!head) return;

    // 1. Find Middle
    let slow = head;
    let fast = head.next;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // 2. Reverse Second Half
    let second = slow.next;
    let prev = slow.next = null;
    while (second) {
        let temp = second.next;
        second.next = prev;
        prev = second;
        second = temp;
    }

    // 3. Merge Two Halves
    let first = head;
    second = prev;
    while (second) {
        let tmp1 = first.next;
        let tmp2 = second.next;
        first.next = second;
        second.next = tmp1;
        first = tmp1;
        second = tmp2;
    }
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
// Test 1: 1->2->3->4
let head1 = createList([1, 2, 3, 4]);
console.log("Original 1:");
printList(head1);
reorderList(head1);
console.log("Reordered 1 (Expected: 1->4->2->3):");
printList(head1);

// Test 2: 1->2->3->4->5
let head2 = createList([1, 2, 3, 4, 5]);
console.log("Original 2:");
printList(head2);
reorderList(head2);
console.log("Reordered 2 (Expected: 1->5->2->4->3):");
printList(head2);
