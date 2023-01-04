class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    stack = []
    res = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right

    return res


def preorder(root):
    stack = [root]
    res = []

    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


    return res

def postorder(root):
    stack = []
    res = []

root = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(6)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(5)
node7 = TreeNode(7)
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


# print(inorder(root))
res = preorder(root)
print(res)
res.reverse()
print(res)
