class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
class SequentialSymbolTable:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def put(self, key, value):
        if self.is_empty():
            self.head = Node(key, value)
            return True
            
        current = self.head
        while current.next is not None:
            if current.key == key:
                current.value = value
                return True
            current = current.next
            
        if current.key == key:
            current.value = value
            return True
                   
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        return True
    
    def get(self, key):
        if self.is_empty():
            return None
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def contains(self, key):
        if self.is_empty():
            return False
        current = self.head
        while current is not None:
            if current.key == key:
                return True
            current = current.next
        return False
    
    def keys(self):
        result = ""
        current = self.head
        while current is not None:
            result += f"Key: {current.key}\n"
            current = current.next
        return result

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += f"Key: {current.key} Value: {current.value}\n"
            current = current.next
        return result