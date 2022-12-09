class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev,current = None,head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev