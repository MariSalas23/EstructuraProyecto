class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BalancedTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        self.update_height(node)
        balance = self.balance_factor(node)

        # Casos de balanceo
        if balance > 1:
            if value < node.left.value:
                return self.right_rotate(node)
            if value > node.left.value:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if value > node.right.value:
                return self.left_rotate(node)
            if value < node.right.value:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:
            return None
        if node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        if not self.root:
            return False
        self.root, deleted = self._delete_recursive(self.root, value)
        return deleted

    def _delete_recursive(self, node, value):
        if not node:
            return node, False

        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right, True
            elif not node.right:
                return node.left, True

            temp = self._find_min(node.right)
            node.value = temp.value
            node.right, _ = self._delete_recursive(node.right, temp.value)
            deleted = True

        if not node:
            return node, deleted

        self.update_height(node)
        balance = self.balance_factor(node)

        # Rebalanceo después de eliminar
        if balance > 1:
            if self.balance_factor(node.left) >= 0:
                return self.right_rotate(node), deleted
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node), deleted

        if balance < -1:
            if self.balance_factor(node.right) <= 0:
                return self.left_rotate(node), deleted
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node), deleted

        return node, deleted

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
        if not node:
            return ""
        result = ""
        result += self._str_recursive(node.right, level + 1)
        result += "  " * level + f"{node.value} (h={node.height})\n"
        result += self._str_recursive(node.left, level + 1)
        return result

    def get_height(self):
        """Retorna la altura del árbol"""
        return self.height(self.root)

    def is_balanced(self):
        """Verifica si el árbol está balanceado"""
        return abs(self.balance_factor(self.root)) <= 1

    def get_level_order(self):
        """Retorna el recorrido por niveles del árbol"""
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            level = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.value)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result
