# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def btreeGameWinningMove(root, n, x):
    """
    :type root: TreeNode
    :type n: int
    :type x: int
    :rtype: bool
    """
    left = 0
    right = 0
    p = findx(root,x)
    if p.left != None:
        left = find(p.left)
    if p.right != None:
        right = find(p.right)
    if max(left,right,n-1-left-right) >= (n+1)/2:
        return True
    return False
def find(root):
    if root.left != None and root.right != None:
        return 1 + find(root.left) + find(root.right)
    else:
        if root.left != None and root.right == None:
            return 1 + find(root.left)
        else:
            if root.left == None and root.right != None:
                return 1 + find(root.right)
            else:
                return 1        
def findx(root,x):
    if root.val == x:
        return root
    else:
        if root.left == None and root.right == None:
            return None
        if root.left == None and root.right != None:
            return findx(root.right,x)
        if root.right == None and root.left != None:
            return findx(root.left,x)
        if root.left != None and root.right != None:
            l = findx(root.left,x)
            r = findx(root.right,x)
            if l != None:
                return l
            if r != None:
                return r
            return None


# tree = [0] * 13
# for i in range(1,12):
#     tree[i] = TreeNode(i)
# for i in range(1,12):
#     if tree[i].val * 2 <= 11:
#         tree[i].left = tree[tree[i].val * 2]
#     if tree[i].val * 2 + 1 <= 11:
#         tree[i].right = tree[tree[i].val * 2 + 1]
#
# print(btreeGameWinningMove(tree[1],11,2))
tree = [0] * 7
tree[0] = TreeNode(3)
tree[1] = TreeNode(6)
tree[2] = TreeNode(7)
tree[3] = TreeNode(4)
tree[4] = TreeNode(1)
tree[5] = TreeNode(2)
tree[6] = TreeNode(5)
tree[0].right = tree[1]
tree[1].right = tree[2]
tree[2].left = tree[3]
tree[3].left = tree[4]
tree[3].right = tree[5]
tree[5].left = tree[6]
print(btreeGameWinningMove(tree[0],7,4))