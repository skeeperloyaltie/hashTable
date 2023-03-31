import time 
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        
    def hash(self, key):
        return hash(key) % self.size
        
    def insert(self, key, value):
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        
    def get(self, key):
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)
        
def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

english_small = read_file('english_small.txt.txt')
english_large = read_file('english_large.txt')

for size in [200000, 300000, 400000]:
    hash_table = HashTable(size)
    
    start_time = time.time()
    for word in english_small:
        hash_table.insert(word, True)
    end_time = time.time()
    print(f"Hash table size: {size}, Time taken to insert small dictionary: {end_time-start_time}")
    
    start_time = time.time()
    for word in english_large:
        hash_table.insert(word, True)
    end_time = time.time()
    print(f"Hash table size: {size}, Time taken to insert large dictionary: {end_time-start_time}")
