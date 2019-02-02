# 1. [easy] 563.Binary Tree Tilt


class BinaryTreeTilt:
    tilt = 0

    def findTilt(self, root):
        self.traverse(root)
        return self.tilt

    def traverse(self, root):
        if root == None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left-right)
        return root.val + left + right


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


'''
test:
    a = Node(3,None,None)
    b = Node(1,None,None)
    c = Node(6,None,None)
    d = Node(5,None,None)
    e = Node(2,a,b)
    f = Node(4,c,d)
    g = Node(3,e,f)
    
    res = BinaryTreeTilt().findTilt(g)
    print(res)
'''