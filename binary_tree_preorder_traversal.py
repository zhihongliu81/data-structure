def preorderTraversal(root):
    # if not root:
    #     return []
    # res = []
    # def helper(node):
    #     res.append(node.val)
    #     if node.left:
    #         helper(node.left)
    #     if node.right:
    #         helper(node.right)

    # helper(root)
    # return res

    if not root:
        return []
    nodes = [root]
    res = []
    while nodes:
        node = nodes.pop()
        res.append(node.val)
        if node.right:
            nodes.append(node.right)
        if node.left:
            nodes.append(node.left)

    return res
