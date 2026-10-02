# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        queue = deque()
        if root:
            queue.append((root, root.val))
        while queue:
            node, mval = queue.popleft()
            if node.val >= mval:
                res += 1
            if node.left:
                queue.append((node.left, max(mval, node.val)))
            if node.right:
                queue.append((node.right, max(mval, node.val)))
        return res
