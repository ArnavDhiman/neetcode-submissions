# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_map = {}
        self.inorder = inorder
        self.preorder = preorder
        self.pre_idx = 0
        for i, v in enumerate(inorder):
            self.inorder_map[v] = i
        
        return self.recur(0, len(inorder)-1)

    def recur(self, inorder_start, inorder_end):
        if inorder_start > inorder_end or self.pre_idx >= len(self.preorder):
            return None
        node = TreeNode(self.preorder[self.pre_idx])
        self.pre_idx += 1
        inorder_idx = self.inorder_map[node.val]
        node.left = self.recur(inorder_start, inorder_idx-1)
        node.right = self.recur(inorder_idx+1, inorder_end)
        return node