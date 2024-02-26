# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        else:
            def travel(root):
                if root.left is not None and root.right is not None:
                    temp=root.left
                    root.left=root.right
                    root.right=temp
                    travel(root.right)
                    travel(root.left)
                elif root.left is None and root.right is not None:
                    root.left=root.right
                    root.right=None
                    travel(root.left)
                elif root.left is not None and root.right is None:
                    root.right=root.left
                    root.left=None
                    travel(root.right)
            travel(root)
            return root