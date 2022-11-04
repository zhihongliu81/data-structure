"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    carrier = 0
    res = curr = ListNode()
    while l1 or l2:
        nxt = ListNode()
        curr.next = nxt
        curr =nxt
        num1 = num2 = 0
        if l1:
            num1 = l1.val
            l1 = l1.next
        if l2:
            num2 = l2.val
            l2 = l2.next
        sum1 = num1 + num2 + carrier
        carrier, remainder = divmod(sum1, 10)
        curr.val = remainder

    if carrier:
        curr.next = ListNode(1)

    return res.next
