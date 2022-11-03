"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""


def hasPathSum( root, targetSum):
        # if root == None:
        #     return False
        # sum_nodes = [[root, root.val]]
        # while sum_nodes:
        #     curr_sum_node = sum_nodes.pop()
        #     curr_node = curr_sum_node[0]
        #     curr_sum = curr_sum_node[1]
        #     if (curr_node.left == None and
        #         curr_node.right == None and
        #         curr_sum == targetSum):
        #         return True
        #     else:
        #         if curr_node.left:
        #             sum_nodes.append([curr_node.left, curr_sum + curr_node.left.val])
        #         if curr_node.right:
        #             sum_nodes.append([curr_node.right, curr_sum + curr_node.right.val])

        # return False

        if root == None:
            return False

        if (root.left == None and
            root.right == None and
            root.val == targetSum):
            return True

        targetSum -= root.val

        return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
