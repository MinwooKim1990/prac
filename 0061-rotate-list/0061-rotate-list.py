# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=head
        nod=[]
        while a != None:
            nod.append(a.val)
            a=a.next
        if len(nod)==0:
            return head
        elif k > len(nod):
            k=k%len(nod)
        nod1=nod[:-k]
        nod2=nod[-k:]
        node=nod2+nod1
        b=ListNode(node[-1])
        for i in range(len(node)-1):
            c=ListNode()
            c.next=b
            c.val=node[-i-2]
            b=c
        return b
        