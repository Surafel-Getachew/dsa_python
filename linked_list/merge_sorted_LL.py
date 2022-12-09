class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        currentRes = res
        while list1 and list2:
            if list1.val < list2.val:
                currentRes.next = list1
                list1 = list1.next
            else:
                currentRes.next = list2
                list2 = list2.next
            currentRes = currentRes.next
        if list1 == None:
            currentRes.next = list2
        else:
            currentRes.next = list1
        return res.next