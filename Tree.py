class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None

def init_tree():
    global root
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    node = root.left
    node.left = Node("D")
    node.right = Node("E")
    node = root.right
    node.left = Node("F")
    node.right = Node("G")

def preorder_traverse(node):
    if node == None: return
    print(node.data, end='->')
    preorder_traverse(node.left)
    preorder_traverse(node.right)

def inorder_traverse(node):
    if node==None: return
    inorder_traverse(node.left)
    print(node.data, end='->')
    inorder_traverse(node.right)

def postorder_traverse(node):
    if node==None: return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.data, end='->')

if __name__ == "__main__":
    global root
    init_tree()
    preorder_traverse(root)
    print("")
    inorder_traverse(root)
    print("")
    postorder_traverse(root)