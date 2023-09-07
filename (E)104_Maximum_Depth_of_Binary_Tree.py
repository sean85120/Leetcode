# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# the max depth
res = 0
# current depth
depth = 0


# main function
def maxDepth(root: TreeNode) -> int:
    traverse(root)
    return res


# binary tree traversal framework
def traverse(root: TreeNode) -> None:
    global res, depth

    if not root:
        return
    # front order position
    depth += 1
    if not root.left and not root.right:
        # update res
        res = max(res, depth)
    traverse(root.left)
    traverse(root.right)
    # back order position
    depth -= 1


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(maxDepth(root))
