class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def push(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            
        if self.first is None:
            self.first = new_node
        self.size += 1
    
    def pop(self):
        if self.first is None:
            raise IndexError("Queue is empty")
        
        data = self.first.data
        self.first = self.first.next
        self.size -= 1
        
        if self.first is None:
            self.last = None
            
        return data
    
    def peek(self):
        if self.first is None:
            raise IndexError("Queue is empty")
        return self.first.data
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.first is None:
            return "Queue is empty"
        
        elements = []
        current = self.first
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return " <- ".join(elements)
        
if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(f"Queue state: {queue}")
    print(f"Popped: {queue.pop()}")
    print(f"Queue state after pop: {queue}")