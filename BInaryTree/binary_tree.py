class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursivve(self.root, data) 

    def _insert_recursivve(self, node, data) -> None:
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursivve(node.data, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursivve(node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)


tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(10))  # True
print(tree.search(7))   # False
print(tree.search(15))  # True