# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        a, b, c = self.dfs(root)
        return b
    def dfs(self, root):
        if root.left is None and root.right is None:
            return root.val, 1, 1
        elif root.left is None:
            sum, res, num = self.dfs(root.right)
            if (root.val + sum) / (num + 1) == root.val:
                return root.val + sum, res + 1, num + 1
            else:
                return root.val + sum, res, num + 1
        elif root.right is None:
            sum, res, num = self.dfs(root.left)
            if (root.val + sum) / (num + 1) == root.val:
                return root.val + sum, res + 1, num + 1
            else:
                return root.val + sum, res, num + 1
        else:
            lsum, lres, lnum = self.dfs(root.left)
            rsum, rres, rnum = self.dfs(root.right)
            if (root.val + lsum + rsum) / (lnum + rnum + 1) == root.val:
                return root.val + lsum + rsum, lres + rres + 1, lnum + rnum + 1
            else:
                return root.val + lsum + rsum, lres + rres, lnum + rnum + 1
