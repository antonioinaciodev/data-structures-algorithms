class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        return True
    
    def pop(self):
        if self.size > 0:
            popped_node = self.top
            self.top = self.top.next
            self.size -= 1
            return popped_node.data
        raise IndexError("Stack is empty!")
    
    def peek(self):
        if self.size > 0:
            return self.top.data
        raise IndexError("Stack is empty!")
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        elements = []
        current = self.top
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return "\n".join(elements)
    
if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack elements (top to bottom):")
    print(stack)
    print(f"Popped: {stack.pop()}")
    print(f"Current top: {stack.peek()}")