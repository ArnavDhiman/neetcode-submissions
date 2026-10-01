# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        mp = {None:0}
        stack = []
        if root:
            mp[root] = 1
            stack.append(root)

        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                mp[node.left] = 0
                stack.append(node.left)
                continue
            if node.right and node.right not in mp:
                mp[node.right] = 0
                stack.append(node.right)
                continue

            node = stack.pop()
            mp[node] = max(mp[node.left], mp[node.right]) + 1
            # print(node.left, node.right, mp[node.left], mp[node.right])
            if -1 <= mp[node.left] - mp[node.right] <= 1:
                continue
            return False
        return True