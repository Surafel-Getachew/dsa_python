# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head.next == None:
        return None
    store = []
    current = head
    while current:
        store.append(current)
        current = current.next

    prevIndex = len(store) - n - 1
    if prevIndex < 0:
        head = head.next
    else:
        prevNode = store[prevIndex]
        prevNode.next = prevNode.next.next
    return head
