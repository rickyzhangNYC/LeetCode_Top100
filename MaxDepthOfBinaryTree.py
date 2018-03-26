counter = 0
def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    if root.left == None and root.Right == None:
        return 1
    return max(self.maxDepth(root.left),self.maxDepth(root.right))+1


    # left_depth = 0
    # right_depth = 0
    # if root == None:
    #     return 0
    # if root.left != None:
    #     left_depth = self.maxDepth(root.left)
    # if root.right != None:
    #     right_depth = self.maxDepth(root.right)
    # if left_depth>right_depth:
    #     return left_depth+1
    # else:
    #     return right_depth+1