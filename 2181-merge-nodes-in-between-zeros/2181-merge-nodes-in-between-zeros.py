# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        v=head.val
        while head != None:
            head=head.next
            if head == None:
                break
            v+=head.val
            if head.val == 0:
                res.append(v)
                v=0
        res2=ListNode(0)
        for i in range(len(res)):
            res2.val=res[-i-1]
            res2=ListNode(0,res2)  
        return res2.next
            