# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mp = {None: 0}
        stack = []
        res = 0
        if root:
            mp[root] = 0
            stack.append(root)
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
                mp[node.left] = 0
                continue
            if node.right and node.right not in mp:
                stack.append(node.right)
                mp[node.right] = 0
                continue
            node = stack.pop()
            res = max(mp[node.left]+mp[node.right], res)
            mp[node] = max(mp[node.left], mp[node.right])+1
            
            # print(mp)
        return res
            