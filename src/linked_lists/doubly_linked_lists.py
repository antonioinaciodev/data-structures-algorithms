class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_sorted(self, data):
        # Tratamento para strings que você tinha implementado antes
        if isinstance(data, str):
            data = data.upper()
            
        if self.contains(data):
            print(f"Value '{data}' already registered.")
            return False
            
        new_node = DoubleNode(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if data < self.head.data:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                current = self.head
                while current.next is not None and current.next.data < data:
                    current = current.next
                
                new_node.next = current.next
                new_node.prev = current
                
                if current.next is not None:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                
                current.next = new_node
        self.size += 1
        return True

    def contains(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def remove(self, data):
        if self.head is None:
            print("Empty list.")
            return False
            
        current = self.head
        if current.data == data:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None 
            self.size -= 1
            return True
            
        while current is not None:
            if current.data == data:
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                if current.prev is not None:
                    current.prev.next = current.next
                self.size -= 1
                return True
            current = current.next
            
        print(f"Value '{data}' not found.")
        return False

    def __str__(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return " <-> ".join(elements) + f" (Total items: {self.size})"

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_sorted(5)
    dll.insert_sorted(3)
    dll.insert_sorted(8)
    dll.insert_sorted(1)
    dll.insert_sorted(4)
    
    print("Doubly Linked List:")
    print(dll)
    
    print("\nContains 3?", dll.contains(3))
    print("Contains 7?", dll.contains(7))
    
    print("\nRemoving 3...")
    dll.remove(3)
    print(dll)
    
    print("\nAttempting to remove 10...")
    dll.remove(10)