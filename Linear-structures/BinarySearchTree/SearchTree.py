class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left is None:
                        current.left = new_node
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        return
                    current = current.right

    def find(self, val):
        current = self.root
        while current is not None:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, val):
        # Find the node to delete
        current = self.root
        parent = None
        is_left = True
        while current is not None:
            if current.val == val:
                break
            elif val < current.val:
                parent = current
                current = current.left
                is_left = True
            else:
                parent = current
                current = current.right
                is_left = False

        # If the node is not found, there is nothing to do
        if current is None:
            return False

        # If the node has both children, find the in-order successor
        if current.left is not None and current.right is not None:
            successor = current.right
            successor_parent = current
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            # Replace the value of the node we want to delete with the value of the successor
            current.val = successor.val

            # Now we want to delete the successor instead of the original node
            current = successor
            parent = successor_parent
            is_left = False

        # If the node has one child or none
        child = current.left if current.left is not None else current.right
        if child is not None:
            child.parent = parent

        # If the node we want to delete is the root
        if parent is None:
            self.root = child
        elif is_left:
            parent.left = child
        else:
            parent.right = child

        return True


    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val)


Tree=BinarySearchTree()
Tree.insert(1)
Tree.insert(2)
Tree.insert(5)
Tree.insert(8)
Tree.insert(6)
Tree.insert(3)
Tree.insert(0)
Tree.inorder()

