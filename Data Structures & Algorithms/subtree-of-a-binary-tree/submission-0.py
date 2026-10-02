# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        
        while stack:
            n1 = stack.pop()
            if not n1:
                continue
            if n1.val == subRoot.val:
                if self.is_sub(n1, subRoot):
                    return True
            stack.append(n1.left)
            stack.append(n1.right)
        return False

    def is_sub(self, root, subroot):
        stack = [(root, subroot)]

        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))
        return True