import time

# Function to read the dictionary file and store words in a hash table
def read_dictionary(file_name, hash_size):
    hash_table = [None] * hash_size
    with open(file_name) as f:
        for line in f:
            word = line.strip()
            hash_key = hash(word) % hash_size
            if hash_table[hash_key] is None:
                hash_table[hash_key] = [word]
            else:
                hash_table[hash_key].append(word)
    return hash_table

# Dictionary file names
small_dict = "english_small.txt.txt"
large_dict = "english_large.txt"

# Hash table sizes to test
hash_sizes = [200000, 300000, 400000]

# Measure time to read and store words in hash table for small dictionary
print("Small dictionary:\n")
for size in hash_sizes:
    start_time = time.time()
    hash_table = read_dictionary(small_dict, size)
    end_time = time.time()
    print(f"Hash table size: {size}\nTime taken: {end_time - start_time:.3f} seconds\n")

# Measure time to read and store words in hash table for large dictionary
print("Large dictionary:\n")
for size in hash_sizes:
    start_time = time.time()
    hash_table = read_dictionary(large_dict, size)
    end_time = time.time()
    print(f"Hash table size: {size}\nTime taken: {end_time - start_time:.3f} seconds\n")
