# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root, p=1, gp=1):
        return self.sumEvenGrandparent(root.left, root.val, p) \
            + self.sumEvenGrandparent(root.right, root.val, p) \
            + root.val * (1 - gp % 2) if root else 0
            
                