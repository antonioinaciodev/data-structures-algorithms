class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    def __str__(self):
        string = f"Key: {self.key}"
        if self.left:
            string += f" - Left child: {self.left.key}"
        if self.right:
            string += f" - Right child: {self.right.key}"
        return string

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def add(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        
        previous = None
        current = self.root
        
        while current:
            if key > current.key:
                previous = current
                current = current.right
            elif key < current.key:
                previous = current
                current = current.left
            else:
                return # Key already exists
            
        if key > previous.key:
            previous.right = Node(key)
        else:
            previous.left = Node(key)

    def show_in_order(self, root):
        if root is None:
            return []
        return self.show_in_order(root.left) + [root.key] + self.show_in_order(root.right)
    
    def show_pre_order(self, root):
        if root is None:
            return []
        return [root.key] + self.show_pre_order(root.left) + self.show_pre_order(root.right)
            
    def show_post_order(self, root):
        if root is None:
            return []
        return self.show_post_order(root.left) + self.show_post_order(root.right) + [root.key]
    
    def show_level_order(self, root):
        height = self.height(root)
        result = []
        for i in range(1, height + 1):
            result.extend(self.get_current_level(root, i))
        return result
    
    def get_current_level(self, root, level):
        if root is None:
            return []
        if level == 1:
            return [root.key]
        elif level > 1:
            return self.get_current_level(root.left, level - 1) + self.get_current_level(root.right, level - 1)
        
    def size(self, root):
        if root is None:
            return 0
        return 1 + self.size(root.left) + self.size(root.right)

    def height(self, root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)
    
    def min_value(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current.key
    
    def max_value(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current.key
    
    def internal_path_length(self, root, depth=0):
        if root is None:
            return 0
        return depth + self.internal_path_length(root.left, depth + 1) + self.internal_path_length(root.right, depth + 1)
    
    def is_balanced(self, root):
        if root is None:
            return True
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return self.is_balanced(root.left) and self.is_balanced(root.right)

if __name__ == '__main__':
    bst = BinarySearchTree()
    
    # Building the tree
    keys_to_add = [15, 20, 11, 10, 7, 21, 59, 99, 13]
    for key in keys_to_add:
        bst.add(key)
        
    print(f"Tree built with keys: {keys_to_add}\n")
    
    print("--- Traversals ---")
    print(f"In-order:    {bst.show_in_order(bst.root)}")
    print(f"Pre-order:   {bst.show_pre_order(bst.root)}")
    print(f"Post-order:  {bst.show_post_order(bst.root)}")
    print(f"Level-order: {bst.show_level_order(bst.root)}\n")
    
    print("--- Tree Metrics ---")
    print(f"Size: {bst.size(bst.root)} nodes")
    print(f"Height: {bst.height(bst.root)}")
    print(f"Min value: {bst.min_value(bst.root)}")
    print(f"Max value: {bst.max_value(bst.root)}")
    print(f"Internal path length: {bst.internal_path_length(bst.root)}")
    print(f"Is balanced? {'Yes' if bst.is_balanced(bst.root) else 'No'}")