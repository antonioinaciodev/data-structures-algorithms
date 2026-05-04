class BinarySearchSymbolTable:
    def __init__(self):
        self.keys = []
        self.values = []
        
    def is_empty(self):
        return len(self.keys) == 0
    
    def binary_search(self, key):
        low = 0
        high = len(self.keys) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.keys[mid] == key:
                return mid
            elif self.keys[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def put(self, key, value):
        pos = self.binary_search(key)
        if pos != -1:
            self.values[pos] = value
            return True
        else:
            self.keys.append(key)
            self.keys.sort()
            new_pos = self.binary_search(key)
            self.values.insert(new_pos, value)
    
    def __str__(self):
        result = ""
        for i in range(len(self.keys)):
            result += f"Key: {self.keys[i]} - Value: {self.values[i]}\n"
        return result