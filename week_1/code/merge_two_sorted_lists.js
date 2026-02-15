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
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
    let dummy = new ListNode();
    let tail = dummy;

    while (list1 && list2) {
        if (list1.val < list2.val) {
            tail.next = list1;
            list1 = list1.next;
        } else {
            tail.next = list2;
            list2 = list2.next;
        }
        tail = tail.next;
    }

    if (list1) {
        tail.next = list1;
    } else if (list2) {
        tail.next = list2;
    }

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
    let dummy = new ListNode();
    let curr = dummy;
    for (let val of arr) {
        curr.next = new ListNode(val);
        curr = curr.next;
    }
    return dummy.next;
}

// Test cases
let l1 = createList([1, 2, 4]);
let l2 = createList([1, 3, 4]);
console.log("List 1:");
printList(l1);
console.log("List 2:");
printList(l2);
let merged = mergeTwoLists(l1, l2);
console.log("Merged (Expected: 1->1->2->3->4->4):");
printList(merged);
