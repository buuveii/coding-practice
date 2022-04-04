class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data
    
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.val)
            res = res + self.inorder_traversal(root.right)

        return res

    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)

        return res
    
    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.val)
        
        return res

def main():
    root = Node(10)
    root.insert(9)
    root.insert(15)
    root.insert(7)
    root.insert(2)
    root.insert(23)
    print("Following is the in-order traversal")
    print(root.inorder_traversal(root))
    print("Following is the pre-order traversal")
    print(root.preorder_traversal(root))
    print("Following is the post-order traversal")
    print(root.postorder_traversal(root))

if __name__ == '__main__':
    main()