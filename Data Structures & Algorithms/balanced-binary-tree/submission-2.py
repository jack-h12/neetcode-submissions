# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root):
        if root == None:
            return 0
        else:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
            return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
            height_difference = abs(left_height - right_height)
            if height_difference > 1:
                is_balanced = False
            else:
                is_balanced = True
            return is_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)


    