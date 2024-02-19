# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_number):
            if not node:
                return 0
            # Update the current number. Shift left (multiply by 2) and add the node's value.
            current_number = (current_number << 1) | node.val
            # If it's a leaf node, return the current number.
            if not node.left and not node.right:
                return current_number
            # Recursively call dfs for left and right children, and return their sum.
            return dfs(node.left, current_number) + dfs(node.right, current_number)

        # Start DFS with the root node and initial number of 0.
        return dfs(root, 0)