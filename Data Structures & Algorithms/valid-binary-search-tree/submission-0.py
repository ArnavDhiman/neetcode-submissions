# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        MIN_VAL = -1000000001
        MAX_VAL = 1000000001

        stack = []
        if root:
            stack.append((root, MIN_VAL, MAX_VAL))
        while stack:
            node, minval, maxval = stack.pop()
            # print(node.val, minval, maxval)
            if not(minval < node.val < maxval):
                return False
            if node.left:
                stack.append((node.left, minval, node.val))
            if node.right:
                stack.append((node.right, node.val, maxval))
            
        return True