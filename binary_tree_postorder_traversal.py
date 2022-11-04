class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def postorderTraversal(root):
    # if not root:
    #     return []
    # res = []
    # def helper(node):
    #     if node.left:
    #         helper(node.left)
    #     if node.right:
    #         helper(node.right)

    #     res.append(node.val)

    # helper(root)
    # return res

    if not root:
        return []
    res = []
    nodes = [root]
    count = 8
    while nodes and count > 0:
        count -= 1
        curr = nodes.pop()
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]

root = TreeNode(0)
node1 = TreeNode(2)
node2 = TreeNode(3)

root.right = node1
node1.left = node2

print(postorderTraversal(root))
