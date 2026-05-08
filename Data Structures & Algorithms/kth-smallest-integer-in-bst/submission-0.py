# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        ans, idx = 0, 0
        def inOrder(root):
            nonlocal ans, idx

            if not root:
                return
            
            inOrder(root.left)
            idx+=1
            if idx == k: ans = root.val
            inOrder(root.right)
        inOrder(root)
        return ans