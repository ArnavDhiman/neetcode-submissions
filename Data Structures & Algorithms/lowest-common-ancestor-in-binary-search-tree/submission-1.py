# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = {}
        res = root
        p_height = q_height = -1
        stack = [(root,0)]
        while stack:
            node, lvl = stack.pop()
            if not node:
                continue
            if node == p:
                p_height = lvl
            if node == q:
                q_height = lvl
            parent[node.left] = node
            parent[node.right] = node
            stack.append((node.left, lvl+1))
            stack.append((node.right, lvl+1))
        # print(parent, p_height, q_height)
        while p_height != q_height:
            if p_height > q_height:
                p = parent[p]
                p_height -= 1 
            if p_height < q_height:
                q = parent[q]
                q_height -= 1
        while p != q:
            p = parent[p]
            q = parent[q]
        
        return p
