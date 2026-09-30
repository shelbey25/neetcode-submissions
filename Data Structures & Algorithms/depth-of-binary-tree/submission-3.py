# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def explore(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        explore_val = 0
        if root.left:
            explore_val = self.explore(root.left)+1
        if root.right:
            right_val = self.explore(root.right)+1
            if explore_val < right_val:
                explore_val = right_val
        return explore_val
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;
        return self.explore(root)
        