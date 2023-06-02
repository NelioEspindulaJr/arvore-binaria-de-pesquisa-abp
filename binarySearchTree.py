from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert_recursive(self.root, value)

    def search(self, value):
        return self.__search_recursive(self.root, value)

    def remove(self, value):
        self.root = self.__remove_recursive(self.root, value)

    def inorder_traversal(self):
        self.__inorder_traversal_recursive(self.root)

    def print_tree(self):
        self.__print_tree_recursive(self.root, 0)

    def inorder_traversal(self):
        self.__inorder_traversal_recursive(self.root)

    def postorder_traversal(self):
        self.__postorder_traversal_recursive(self.root)

    def preorder_traversal(self):
        self.__preorder_traversal_recursive(self.root)

    def level_order_traversal(self):
        if self.root is None:
            return

        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.value, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    def print_first_four_levels(self):
        if self.root is None:
            return

        queue = deque()
        queue.append((self.root, 0))

        current_level = 0
        while queue:
            node, level = queue.popleft()

            if level > 4:
                break

            if level > current_level:
                print()  # Iniciar nova linha para cada novo nível
                current_level = level

            print(node.value, end=" ")

            if node.left is not None:
                queue.append((node.left, level + 1))

            if node.right is not None:
                queue.append((node.right, level + 1))

    def __preorder_traversal_recursive(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.__preorder_traversal_recursive(node.left)
            self.__preorder_traversal_recursive(node.right)

    def __postorder_traversal_recursive(self, node):
        if node is not None:
            self.__postorder_traversal_recursive(node.left)
            self.__postorder_traversal_recursive(node.right)
            print(node.value, end=" ")

    def __inorder_traversal_recursive(self, node):
        if node is not None:
            self.__inorder_traversal_recursive(node.left)
            print(node.value, end=" ")
            self.__inorder_traversal_recursive(node.right)

    def __print_tree_recursive(self, node: Node, level=0):
        if node is not None:
            if node.right:
                self.__print_tree_recursive(node.right, level + 1)
            print("    " * level + str(node.value))
            if node.left:
                self.__print_tree_recursive(node.left, level + 1)

    def __inorder_traversal_recursive(self, node: Node):
        if node is not None:
            self.__inorder_traversal_recursive(node.left)
            print(node.value, end=" ")
            self.__inorder_traversal_recursive(node.right)

    def __remove_recursive(self, node: Node, value):
        if node is None:
            return node
        if int(value) < node.value:
            node.left = self.__remove_recursive(node.left, value)
        elif int(value) > node.value:
            node.right = self.__remove_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.value = self.__find_min_value(node.right)
            node.right = self.__remove_recursive(node.right, node.value)
        return node

    def __find_min_value(self, node: Node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def __search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self.__search_recursive(node.left, value)
        return self.__search_recursive(node.right, value)

    def __insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__insert_recursive(node.right, value)
