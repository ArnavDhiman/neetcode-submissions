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
        queue = deque()
        if root:
            queue.append((root, MIN_VAL, MAX_VAL))
        while queue:
            node, minval, maxval = queue.popleft()
            # print(node.val, minval, maxval)
            if not(minval < node.val < maxval):
                return False
            if node.left:
                queue.append((node.left, minval, node.val))
            if node.right:
                queue.append((node.right, node.val, maxval))
            
        return True