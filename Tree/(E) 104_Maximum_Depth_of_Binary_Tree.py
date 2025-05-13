# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, res: int, depth: int):
        # the max depth
        self.res = res
        # current depth
        self.depth = depth

    # main function
    def maxDepth(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.res

    # binary tree traversal framework
    def traverse(self, root: TreeNode) -> None:

        if not root:
            return
        # front order position
        self.depth += 1
        if not root.left and not root.right:
            # update res
            self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)
        # back order position
        self.depth -= 1


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.maxDepth(root))
