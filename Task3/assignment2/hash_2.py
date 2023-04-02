import sys
import time

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))
        
    def find(self, key):
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found in hash table.")
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python hash_table.py <dictionary_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    sizes = [200000, 300000, 400000]
    
    for size in sizes:
        hash_table = HashTable(size)
    
        start_time = time.time()
        with open(filename, 'r') as f:
            for line in f:
                key = line.strip()
                hash_table.insert(key, None)
        end_time = time.time()
    
        elapsed_time = end_time - start_time
        print(f"Hash table size: {size}\nElapsed time: {elapsed_time:.2f} seconds\n")
