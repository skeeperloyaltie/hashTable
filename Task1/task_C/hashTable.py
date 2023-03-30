class HashTable:
    def __init__(self, size):
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
        if None not in self.keys:
            raise Exception("Hash table is full.")
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def hash(self, key):
        # Custom hash function
        # Convert the key to a string and sum the ASCII codes of its characters
        # Multiply the sum by a large prime number and take the remainder
        return sum(ord(c) for c in str(key)) * 101 % self.size

def main():
    # Create a hash table with size 10
    table = HashTable(10)

    # Insert some key-value pairs
    table['apple'] = 1
    table['banana'] = 2
    table['cherry'] = 3

    # Get some values by key
    print(table['apple'])   # Output: 1
    print(table['banana'])  # Output: 2

    # Check if some keys are in the table
    print('apple' in table)    # Output: True
    print('durian' in table)   # Output: False

if __name__ == '__main__':
    main()
