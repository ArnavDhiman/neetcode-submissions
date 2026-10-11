# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        queue = deque()
        if root:
            queue.append(root)
            res.append(str(root.val))
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                res.append(str(node.left.val))
            else:
                res.append(str(None))
            if node.right:
                queue.append(node.right)
                res.append(str(node.right.val))
            #right
            else:
                res.append(str(None))
        # print(res)
        return "-".join(res)
            


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        head = None
        if not data:
            return head
        l_data = data.split("-")
        queue = deque()
        head = TreeNode(int(l_data[0]))
        queue.append((head))
        child = 0
        while queue:
            # print(queue)
            node = queue.popleft()
            left = child+1
            if left < len(l_data) and l_data[left]!="None":
                node.left = TreeNode(l_data[left])
                queue.append((node.left))
                
            right = left + 1
            if left < len(l_data) and l_data[right]!="None":
                node.right = TreeNode(l_data[right])
                queue.append((node.right))
            child += 2
        return head