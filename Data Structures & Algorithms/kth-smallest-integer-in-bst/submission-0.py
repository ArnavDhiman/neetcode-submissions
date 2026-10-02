# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        p = {}
        stack = []
        res = 0

        if root:
            stack.append(root)
            p[root] = 0
        while stack:
            node = stack[-1]
            if node.left and node.left not in p:
                p[node.left] = 0
                stack.append(node.left)
                continue
                
            node = stack.pop(-1)
            res += 1
            # print(node.val, res, k)
            if res == k:
                return node.val
            if node.right and node.right not in p:
                p[node.right] = 0
                stack.append(node.right)
                continue
        return -1