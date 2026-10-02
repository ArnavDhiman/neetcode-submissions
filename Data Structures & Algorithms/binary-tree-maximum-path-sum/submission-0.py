# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mp = {None:0}
        stack = []
        res = -1001
        if root:
            stack.append(root)
            mp[root] = 0

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
            l = mp[node.left]
            r = mp[node.right]
            mp[node] = max(node.val, max(l,r)+node.val)
            res = max(res, mp[node], l+r+node.val)
            # print(l,r,node.val,res,mp[node])
        # print(mp)
        return res
