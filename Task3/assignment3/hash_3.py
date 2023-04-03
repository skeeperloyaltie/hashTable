import random
import statistics

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.count = 0

    def hash_func(self, key):
        return key % self.size

    def hash_func2(self, key):
        return 1 + (key % (self.size - 1))

    def rehash_linear(self, old_hash, i):
        return (old_hash + i) % self.size

    def rehash_quadratic(self, old_hash, i):
        return (old_hash + i**2) % self.size

    def rehash_double(self, old_hash, i):
        return (old_hash + i * self.hash_func2(old_hash)) % self.size

    def put(self, key):
        if self.count == self.size:
            raise Exception("Hash Table is full")
        hash_val = self.hash_func(key)
        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.count += 1
        else:
            for i in range(1, self.size):
                new_hash = self.rehash_linear(hash_val, i)
                if self.slots[new_hash] is None:
                    self.slots[new_hash] = key
                    self.count += 1
                    break

    def put_quadratic(self, key):
        if self.count == self.size:
            raise Exception("Hash Table is full")
        hash_val = self.hash_func(key)
        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.count += 1
        else:
            for i in range(1, self.size):
                new_hash = self.rehash_quadratic(hash_val, i)
                if self.slots[new_hash] is None:
                    self.slots[new_hash] = key
                    self.count += 1
                    break

    def put_double(self, key):
        if self.count == self.size:
            raise Exception("Hash Table is full")
        hash_val = self.hash_func(key)
        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.count += 1
        else:
            for i in range(1, self.size):
                new_hash = self.rehash_double(hash_val, i)
                if self.slots[new_hash] is None:
                    self.slots[new_hash] = key
                    self.count += 1
                    break

    def get(self, key):
        start_slot = self.hash_func(key)
        data = None
        stop = False
        found = False
        position = start_slot
        i = 1
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.slots[position]
            else:
                position = self.rehash_linear(start_slot, i)
                i += 1
                if position == start_slot:
                    stop = True
        return data

def test(probing_technique):
    ht = HashTable(100)
    data = random.sample(range(1, 1500), 1202)
    collisions = 0
    probe_lengths = []
    for key in data:
        try:
            if probing_technique == "linear":
                ht.put(key)
            elif probing_technique == "quadratic":
                ht.put_quadratic(key)
            elif probing_technique == "double":
                ht.put_double(key)
        except:
            collisions += 1
        probe_lengths.append(ht.count)
    avg_probe_length = statistics.mean(probe_lengths)
    return (collisions, avg_probe_length)
     
linear_results = []
quadratic_results = []
double_results = []

for i in range(100):
    linear_results.append(test("linear"))
    quadratic_results.append(test("quadratic"))
    double_results.append(test("double"))

print("Linear probing results:")
print("Number of collisions:", statistics.mean([r[0] for r in linear_results]))
print("Average probe length:", statistics.mean([r[1] for r in linear_results]))
print("\nQuadratic probing results:")
print("Number of collisions:", statistics.mean([r[0] for r in quadratic_results]))
print("Average probe length:", statistics.mean([r[1] for r in quadratic_results]))
print("\nDouble hashing results:")
print("Number of collisions:", statistics.mean([r[0] for r in double_results]))
print("Average probe length:", statistics.mean([r[1] for r in double_results]))
