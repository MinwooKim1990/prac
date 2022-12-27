# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1list=[]
        l2list=[]
        print(l1)
        while l1 != None:
            l1list.append(l1.val)
            l1=l1.next
        l1list=list(reversed(l1list))
        while l2 != None:
            l2list.append(l2.val)
            l2=l2.next
        l2list=list(reversed(l2list))
        num1=int(''.join(map(str,l1list)))
        num2=int(''.join(map(str,l2list)))
        res2=[int(x) for x in str(num1+num2)]
        for i in range(len(res2)):
            if i == 0:
                ress=ListNode(res2[i])
                print(ress)
            else:
                ress=ListNode(res2[i],ress)
        return ress