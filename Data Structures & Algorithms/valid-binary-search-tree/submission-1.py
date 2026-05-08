# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left, right = -float('inf'), float('inf')

        def isValid(root, left, right):
            if not root:
                return True
            
            if left>=root.val or root.val>=right:
                return False
            
            return isValid(root.right, root.val, right) and isValid(root.left, left, root.val)
        
        return isValid(root, left, right)