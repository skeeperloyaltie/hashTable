class hash_T:
    def __init__(self, size=100):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    def __getitem__(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        raise KeyError(key)
        
    def __setitem__(self, key, value):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value
        
    def __contains__(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.size
        return False
        
    def hash(self, key):
        # Custom hash function
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size

def main():
    # Initialize a hash table with a size of 5
    ht = hash_T(5)
    
    # Add some key-value pairs
    ht['apple'] = 5
    ht['banana'] = 3
    ht['cherry'] = 8
    
    # Retrieve values for some keys
    print(ht['apple'])   # Output: 5
    print(ht['cherry'])  # Output: 8
    
    # Check if a key is in the table
    print('banana' in ht)  # Output: True
    print('durian' in ht)  # Output: False
    
    # Try to add a key-value pair when the table is full
    try:
        ht['elderberry'] = 2
    except Exception as e:
        print(e)  # Output: hash table is full
    
    # Update the value for an existing key
    ht['banana'] = 6
    print(ht['banana'])  # Output: 6
    
    # Test the custom hash function
    print(ht.hash('apple'))   # Output: 0
    print(ht.hash('banana'))  # Output: 1
    print(ht.hash('cherry'))  # Output: 3

if __name__ == '__main__':
    main()
