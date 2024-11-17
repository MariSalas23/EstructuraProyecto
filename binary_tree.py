class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        self.root, deleted = self._delete_recursive(self.root, value)
        return deleted

    def _delete_recursive(self, node, value):
        if node is None:
            return None, False
        
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
            return node, deleted
        
        if node.left is None:
            return node.right, True
        elif node.right is None:
            return node.left, True
        
        temp = self._find_min(node.right)
        node.value = temp.value
        node.right, _ = self._delete_recursive(node.right, temp.value)
        return node, True

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def __str__(self):
        if not self.root:
            return "Árbol vacío"
        return self._str_recursive(self.root, 0)

    def _str_recursive(self, node, level):
        if node is None:
            return ""
        result = ""
        result += self._str_recursive(node.right, level + 1)
        result += "  " * level + str(node.value) + "\n"
        result += self._str_recursive(node.left, level + 1)
        return result