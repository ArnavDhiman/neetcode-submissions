# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = set()
        stack = []
        if root:
            stack.append(root)
            seen.add(root)
        while stack:
            node = stack[-1]
            if node.left and node.left not in seen:
                seen.add(node.left)
                stack.append(node.left)
                continue
            node = stack.pop(-1)
            k -= 1
            # print(node.val, res, k)
            if not k:
                return node.val
            if node.right and node.right not in seen:
                seen.add(node.right)
                stack.append(node.right)
                
        return -1