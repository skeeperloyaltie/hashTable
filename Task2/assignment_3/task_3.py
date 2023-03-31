import time
def hash_table(size):
    table = [None] * size

    def hash_func(key):
        return key % size

    def linear_probe(key):
        index = hash_func(key)
        while table[index] is not None:
            index = (index + 1) % size
        return index

    def quadratic_probe(key):
        index = hash_func(key)
        i = 1
        while table[index] is not None:
            index = (index + i**2) % size
            i += 1
        return index

    def double_hash(key):
        index = hash_func(key)
        hash2 = 7 - (key % 7)
        while table[index] is not None:
            index = (index + hash2) % size
        return index

    def insert(key):
        index = quadratic_probe(key)
        table[index] = key

    def search(key):
        index = hash_func(key)
        i = 0
        while table[index] is not None:
            if table[index] == key:
                return index
            index = (index + i**2) % size
            i += 1
        return None

    return {
        'table': table,
        'hash_func': hash_func,
        'linear_probe': linear_probe,
        'quadratic_probe': quadratic_probe,
        'double_hash': double_hash,
        'insert': insert,
        'search': search,
    }


def test_hash_table():
    sizes = [100, 1000, 10000]
    keys = [i for i in range(10001)]

    for size in sizes:
        table = hash_table(size)

        start_time = time.time()
        for key in keys:
            table['insert'](key)
        end_time = time.time()

        probe_lengths = []
        num_collisions = 0
        for key in keys:
            index = table['search'](key)
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
            index = table['quadratic_probe'](key)
            probe_lengths.append(index % size)
            if table['table'][index] is not None:
                num_collisions += 1
            table['table'][index] = key

        print("{:<20} {:<20.2f} {:<20}".format("Quadratic Probing", sum(probe_lengths)/len(probe_lengths), num_collisions))

        probe_lengths = []
        num_collisions = 0
        for key in keys:
            index = table['double_hash'](key)
            probe_lengths.append(index % size)
            if table['table'][index] is not None:
                num_collisions += 1
            table['table'][index] = key

        print("{:<20} {:<20.2f} {:<20}".format("Double Hashing", sum(probe_lengths)/len(probe_lengths), num_collisions))
        print("\n")

def main():
    test_hash_table()


if __name__ == '__main__':
    main()

