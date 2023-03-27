# Test the hash table with optimized read_file function

import time

# Define the hash table class with optimized read_file function
class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    def __setitem__(self, key, value):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value
        
    def __getitem__(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        raise KeyError(key)
        
    def __contains__(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.size
        return False
        
    def hash(self, key):
        """
        My hash function takes a string as input and returns an integer between 0 and size-1.
        The hash value is calculated as the sum of the ASCII values of the characters in the string
        modulo the size of the hash table.
        """
        if isinstance(key, str):
            hash_value = sum(ord(char) for char in key) % self.size
            return hash_value
        else:
            raise TypeError("Key must be a string")
        
def read_file(filename, size):
    # Initialize a hash table with the given size
    table = HashTable(size)
    
    # Open the file and read the lines
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Add the words to the hash table
    for line in lines:
        for word in line.split():
            if word.isalpha():
                if word.lower() in table:
                    table[word.lower()] += 1
                else:
                    table[word.lower()] = 1
    
    return table

# Define the file paths and hash table sizes to test
file_paths = ["english_small.txt", "english_large.txt"]
table_sizes = [200000, 300000, 400000]

# Test the hash table with different file paths and table sizes
for file_path in file_paths:
    for table_size in table_sizes:
        start_time = time.time()
        table = read_file(file_path, table_size)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Reading {file_path} and storing in hash table with size {table_size} took {elapsed_time:.4f} seconds.")
