class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def get(self, key):
        pos = self._hash(key)
        current = self.table[pos]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)
    
    def put(self, key, value):
        pos = self._hash(key)
        if self.table[pos] is None:
            self.table[pos] = Node(key, value)
        else:
            current = self.table[pos]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)
        self.size += 1
        
    def display(self):
        result = ""
        for i, linked_list in enumerate(self.table, 1):
            result += f"\nList {i}:\n"
            if linked_list is None:
                result += "Empty list!"
            else:
                current = linked_list
                j = 1
                while current is not None:
                    result += f"{j} Key: {current.key} Value: {current.value}\n"
                    j += 1
                    current = current.next
        return result