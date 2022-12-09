# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: Optional[ListNode]) -> bool:
    # floyd's tortois and hare
    slow,fast = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

    # This uses extra memory o(n)
    # prev = []
    # currentNode = head
    # while currentNode != None:
    #     if currentNode in prev:
    #         return True
    #     else:
    #         prev.append(currentNode)
    #         currentNode = currentNode.next
    # return False
        
    