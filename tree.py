class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    res = []
    def helper(root):
        if root == None:
            return
        print(root.val)

        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
root.right = node2
node2.left = node3


print(inorderTraversal(root))
