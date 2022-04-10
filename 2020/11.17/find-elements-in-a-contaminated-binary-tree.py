class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements(object):
    s = set()

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        root.val = 0
        self.s.add(0)
        if root.left != None:
            self.build(root.val * 2 + 1, root.left)
        if root.right != None:
            self.build(root.val * 2 + 2, root.right)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.s:
            return True
        else:
            return False

    def build(self, val, node):
        node.val = val
        self.s.add(val)
        if node.left != None:
            self.build(val * 2 + 1, node.left)
        if node.right != None:
            self.build(val * 2 + 2, node.right)

root = TreeNode(-1)
root.right = TreeNode(-1)
root.right.left = TreeNode(-1)
root.right.left.left = TreeNode(-1)

f = FindElements(root)
print(f.find(2))
print(f.find(3))
print(f.find(4))
print(f.find(5))
