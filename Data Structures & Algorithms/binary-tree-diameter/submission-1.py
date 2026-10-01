# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_depth(self, root):
        if not root.right and not root.left:
            return 0
        left = 0
        right = 0
        if root.left:
            left = self.find_depth(root.left)+1
        if root.right:
            right = self.find_depth(root.right)+1
        self.max_diameter = max(self.max_diameter, left+right)
        return max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.find_depth(root), self.max_diameter)
        return max(2 + self.find_depth(root.right) + self.find_depth(root.left), self.max_diameter)