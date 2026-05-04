class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
    def contains(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next 
        return False   
    
    def remove(self, data):
        current = self.head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def __str__(self):
        count = 0
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
            count += 1
        return " -> ".join(elements) + f" (Size: {count})"

if __name__ == '__main__':
    test_list = SinglyLinkedList()
    test_list.add_first(20)
    test_list.add_first(10)
    test_list.add_first(0)
    test_list.add_last(30)
    
    print("List:")
    print(test_list)
    
    print("\nContains 30?", test_list.contains(30))
    print("Contains 50?", test_list.contains(50))
    
    test_list.remove(30)
    print("\nList after removing 30:")
    print(test_list)