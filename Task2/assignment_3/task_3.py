import time

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash(self, key):
        return key % self.size

    def linear_probe(self, key):
        index = self.hash(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        return index

    def quadratic_probe(self, key):
        index = self.hash(key)
        i = 1
        while self.table[index] is not None:
            index = (index + i**2) % self.size
            i += 1
        return index

    def double_hash(self, key):
        index = self.hash(key)
        hash2 = 7 - (key % 7)
        while self.table[index] is not None:
            index = (index + hash2) % self.size
        return index

    def insert(self, key):
        index = self.quadratic_probe(key)
        self.table[index] = key

    def search(self, key):
        index = self.hash(key)
        i = 0
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + i**2) % self.size
            i += 1
        return None


def test_hash_table():
    sizes = [100, 1000, 10000]
    keys = [i for i in range(10001)]

    for size in sizes:
        table = HashTable(size)

        start_time = time.time()
        for key in keys:
            table.insert(key)
        end_time = time.time()

        probe_lengths = []
        num_collisions = 0
        for key in keys:
            index = table.search(key)
            probe_lengths.append(index % size)
            if index is None:
                num_collisions += 1

        print(f"Hash Table Size: {size}")
        print(f"Time Taken: {end_time - start_time:.6f} seconds")
        print("{:<20} {:<20} {:<20}".format("Hash Type", "Probe Length", "Collisions"))
        print("-" * 60)
        print("{:<20} {:<20.2f} {:<20}".format("Linear Probing", sum(probe_lengths)/len(probe_lengths), num_collisions))

        probe_lengths = []
        num_collisions = 0
        for key in keys:
            index = table.quadratic_probe(key)
            probe_lengths.append(index % size)
            if table.table[index] is not None:
                num_collisions += 1
            table.table[index] = key

        print("{:<20} {:<20.2f} {:<20}".format("Quadratic Probing", sum(probe_lengths)/len(probe_lengths), num_collisions))

        probe_lengths = []
        num_collisions = 0
        for key in keys:
            index = table.double_hash(key)
            probe_lengths.append(index % size)
            if table.table[index] is not None:
                num_collisions += 1
            table.table[index] = key

        print("{:<20} {:<20.2f} {:<20}".format("Double Hashing", sum(probe_lengths)/len(probe_lengths), num_collisions))
        print("\n")

test_hash_table()