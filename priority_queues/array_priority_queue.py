class ArrayPriorityQueue:
    def __init__(self, limit):
        self.limit = limit
        self.queue = []
        self.common_count = 0
        self.priority_count = 0
        self.served_common = 0
        self.served_priority = 0
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, name, age):
        if len(self.queue) >= self.limit:
            print("Queue is full. Cannot add more elements.")
            return
            
        if age >= 60:
            self.priority_count += 1
        else:
            self.common_count += 1
            
        self.queue.append((name, age))
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        # Tenta atender um prioritário primeiro
        for i in range(len(self.queue)):
            if self.queue[i][1] >= 60:
                return self._remove_at(i)
        
        # Se não houver prioritário, atende o primeiro comum
        return self._remove_at(0)
    
    def _remove_at(self, index):
        data = self.queue[index]
        del self.queue[index]
        
        if data[1] >= 60:
            self.priority_count -= 1
            self.served_priority += 1
        else:
            self.common_count -= 1
            self.served_common += 1
            
        return data[0]
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0][0]
    
    def total_served(self):
        return self.served_common + self.served_priority
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        for item in self.queue:
            print(f"{item[0]} (Age: {item[1]})")
    
    def show_stats(self):
        print(f"Current common: {self.common_count}")
        print(f"Served common: {self.served_common}")
        print(f"Current priority: {self.priority_count}")
        print(f"Served priority: {self.served_priority}")
    
    def __len__(self):
        return len(self.queue)
    
    def __str__(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return ' '.join([item[0] for item in self.queue])

def main():
    try:
        limit = int(input("Define the queue limit: "))
        queue = ArrayPriorityQueue(limit)
        
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
    except ValueError:
        print("Invalid limit definition.")

if __name__ == '__main__':
    main()