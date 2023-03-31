import time
import random
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, self.size)

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                # collision occurred, probe using quadratic probing
                nextslot = self.rehash_quadratic(hashvalue, self.size)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash_quadratic(nextslot, self.size)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def get(self, key):
        startslot = self.hashfunction(key, self.size)

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash_quadratic(position, self.size)
                if position == startslot:
                    stop = True
        return data

    def hashfunction(self, key, size):
        return key % size

    def rehash_linear(self, oldhash, size):
        return (oldhash + 1) % size

    def rehash_quadratic(self, oldhash, size):
        return (oldhash + 1**2) % size

    def rehash_double(self, oldhash, size):
        return (oldhash + self.hashfunction2(key, size)) % size

    def hashfunction2(self, key, size):
        return 7 - (key % 7)

keys = [random.randint(1, 10000) for i in range(1000)]
data = [random.randint(1, 10000) for i in range(1000)]

linear_probing = HashTable(1000)
quadratic_probing = HashTable(1000)
double_hashing = HashTable(1000)

for i in range(len(keys)):
    linear_probing.put(keys[i], data[i])
    quadratic_probing.put(keys[i], data[i])
    double_hashing.put(keys[i], data[i])

# calculate the number of collisions for each method
linear_collisions = sum([1 for slot in linear_probing.slots if slot != None]) - len(set(linear_probing.slots)) + 1
quadratic_collisions = sum([1 for slot in quadratic_probing.slots if slot != None]) - len(set(quadratic_probing.slots)) + 1
double_collisions = sum([1 for slot in double_hashing.slots if slot != None]) - len(set(double_hashing.slots)) + 1

# calculate the average probe length for each method
linear_probes = sum([len(list(linear_probing.slots)[:linear_probing.slots.index(None)]) for i in range(len(linear_probing.slots)) if linear_probing.slots[i] != None]) / len(keys)
quadratic_probes = sum([len(list(quadratic_probing.slots)[:quadratic_probing.slots.index(None)]) for i in range(len(quadratic_probing.slots)) if quadratic_probing.slots[i] != None]) / len(keys)
double_probes = sum([len(list(double_hashing.slots)[:double_hashing.slots.index(None)]) for i in range(len(double_hashing.slots)) if double_hashing.slots[i] != None]) / len(keys)

# print the results
print("Number of collisions:")
print("Linear probing:", linear_collisions)
print("Quadratic probing:", quadratic_collisions)
print("Double hashing:", double_collisions)
print()
print("Average probe length:")
print("Linear probing:", linear_probes)
print("Quadratic probing:", quadratic_probes)
print("Double hashing:", double_probes)
