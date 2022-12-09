class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if head == None or head.next == None:
        return head
    
    store = []
    current = head
    
    while current:
        store.append(current)
        current = current.next

    left,right = 0,len(store) -1
    while left < right:
        store[left].next = store[right]
        left+=1
        if left == right:
            break
        else:
            store[right].next = store[left]
            right-=1
    
    store[left].next = None