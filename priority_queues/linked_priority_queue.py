class Node:
    def __init__(self, data, age):
        self.data = data
        self.age = age
        self.next = None

class LinkedPriorityQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.common_count = 0
        self.priority_count = 0
        self.served_common = 0
        self.served_priority = 0
    
    def is_empty(self):
        return self.first is None
    
    def enqueue(self, name, age):
        new_node = Node(name, age)
        if self.last is None:
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
            
        if self.first is None:
            self.first = new_node
            
        if age >= 60:
            self.priority_count += 1
        else:
            self.common_count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
            
        current = self.first
        previous = None
        
        # Busca o primeiro prioritário
        while current is not None:
            if current.age >= 60:
                if previous is None:
                    self.first = current.next
                else:
                    previous.next = current.next
                    
                if current == self.last:
                    self.last = previous
                    
                self.priority_count -= 1
                self.served_priority += 1
                return current.data
                
            previous = current
            current = current.next
            
        # Se não achou prioritário, atende o primeiro da fila comum
        data = self.first.data
        self.first = self.first.next
        self.served_common += 1
        self.common_count -= 1
        
        if self.first is None:
            self.last = None
            
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.first.data
        
    def total_served(self):
        return self.served_common + self.served_priority
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.first
        while current is not None:
            print(f"{current.data} (Age: {current.age})")
            current = current.next
    
    def show_stats(self):
        print(f"Current common: {self.common_count}")
        print(f"Served common: {self.served_common}")
        print(f"Current priority: {self.priority_count}")
        print(f"Served priority: {self.served_priority}")
    
    def __len__(self):
        return self.common_count + self.priority_count
    
    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        elements = []
        current = self.first
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return " <- ".join(elements)

def main():
    queue = LinkedPriorityQueue()
    while True:
        try:
            choice = int(input("\nMenu:\n"
                "1 - Add to queue\n"
                "2 - Serve next\n"
                "3 - List queue\n"
                "4 - Service stats\n"
                "5 - Exit\n"
                "Choice: "
                ))
            if choice == 1:
                name = input("Name: ")
                age = int(input("Age: "))
                queue.enqueue(name, age)
            elif choice == 2:
                try:
                    served = queue.dequeue()
                    print(f"{served} was served.")
                except IndexError:
                    print("Queue is empty")
            elif choice == 3:
                queue.display()
            elif choice == 4:
                queue.show_stats()
            elif choice == 5:
                if queue.is_empty():
                    total = queue.total_served()
                    if total > 0:
                        perc_common = (queue.served_common / total) * 100
                        perc_priority = (queue.served_priority / total) * 100
                        print(f"\nTotal served: {total}")
                        print(f"Common served: {perc_common:.2f}%")
                        print(f"Priority served: {perc_priority:.2f}%")
                    break
                else:
                    print("Cannot exit: Queue is not empty!")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    main()