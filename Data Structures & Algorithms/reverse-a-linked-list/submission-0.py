# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sampleArr = []
        current = head
        if head is None:
            return None
        while current:
            sampleArr.append(current.val)
            current = current.next
        sampleArr.reverse()

        new_head = ListNode(sampleArr[0])
        current = new_head
        
        for value in sampleArr[1:]:
            current.next = ListNode(value)
            current = current.next
        
        return new_head