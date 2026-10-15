l1 = [2,4,3]
l2 = [5,6,4]
#807 is the answer
"""
:type l1: Optional[ListNode]
:type l2: Optional[ListNode]
:rtype: Optional[ListNode]
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

dummy = ListNode(0)
curr = dummy
carry = 0

while l1 or l2 or carry:
    x = l1.val if l1 else 0
    y = l2.val if l2 else 0

    total = x + y + carry
    carry = total // 10
    digit = total % 10

    curr.next = ListNode(digit)
    curr = curr.next

    if l1:
        l1 = l1.next
    if l2:
        l2 = l2.next

print(dummy.next)