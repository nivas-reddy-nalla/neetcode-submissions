# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0
        
        def buildTreeHelper(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx
            if left > right:
                return None
            
            val = preorder[preorder_idx]
            preorder_idx += 1
            root_node = TreeNode(val)
            mid = inorder_map[val]
            
            root_node.left = buildTreeHelper(left, mid - 1)
            root_node.right = buildTreeHelper(mid + 1, right)
            
            return root_node
        
        return buildTreeHelper(0, len(inorder) - 1)
            