def minDepth(root):
        if not root:
            return 0
        if not root.left:
            return 1 + minDepth(root.right)
        if not root.right:
            return 1 + minDepth(root.left)


        return 1 + min(minDepth(root.left), minDepth(root.right))



    # if not root:
    #         return 0
    #     levels = [[root]]
    #     count = 1

    #     while levels[0]:
    #         curr_level = levels.pop(0)
    #         next_level = []
    #         for node in curr_level:
    #             if not node.left and not node.right:
    #                 return count
    #             else:
    #                 if node.left:
    #                     next_level.append(node.left)
    #                 if node.right:
    #                     next_level.append(node.right)


    #         levels.append(next_level)
    #         count += 1
