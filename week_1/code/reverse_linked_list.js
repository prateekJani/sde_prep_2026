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
 * @return {ListNode}
 */
var reverseList = function (head) {
    let prev = null;
    let curr = head;
    while (curr) {
        let temp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = temp;
    }
    return prev;
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

// Test cases
// Test 1: 1->2->3->4->5
let head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
console.log("Original:");
printList(head);
let reversedHead = reverseList(head);
console.log("Reversed (Expected: 5->4->3->2->1):");
printList(reversedHead);
