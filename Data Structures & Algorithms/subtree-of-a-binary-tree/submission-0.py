# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def compare(self, root, subroot):
        if not subroot and not root:
            return True
        if not subroot or not root:
            return False
        if root.val != subroot.val:
            return False
        else:
            return self.compare(root.left, subroot.left) and self.compare(root.right, subroot.right)

    def try_nodes(self, root, subroot):
        if self.compare(root, subroot):
            return True
        if root.right and root.left:
            return self.try_nodes(root.right, subroot) or self.try_nodes(root.left, subroot)
        if root.right:
            return self.try_nodes(root.right, subroot)
        if root.left:
            return self.try_nodes(root.left, subroot)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.try_nodes(root, subRoot)
        