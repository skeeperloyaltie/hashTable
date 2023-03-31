class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        
    def __getitem__(self, key):
        hash = self.hash(key)
        while self.keys[hash] != None:
            if self.keys[hash] == key:
                return self.values[hash]
            hash = (hash + 1) % self.size
        raise KeyError(key)
        
    def __setitem__(self, key, value):
        if None not in self.keys:
            raise Exception('Hash table is full')
        hash = self.hash(key)
        while self.keys[hash] != None:
            if self.keys[hash] == key:
                self.values[hash] = value
                return
            hash = (hash + 1) % self.size
        self.keys[hash] = key
        self.values[hash] = value
        
    def __contains__(self, key):
        hash = self.hash(key)
        while self.keys[hash] != None:
            if self.keys[hash] == key:
                return True
            hash = (hash + 1) % self.size
        return False
        
    def hash(self, key):
        # simple hash function that sums the ASCII values of the characters in the key
        # modulo size to keep the hash within the range of the table
        return sum([ord(c) for c in key]) % self.size

def test_hash_table():
    table = HashTable(10)
    
    # test __setitem__ and __getitem__
    table['apple'] = 5
    table['banana'] = 7
    table['cherry'] = 9
    assert table['apple'] == 5
    assert table['banana'] == 7
    assert table['cherry'] == 9
    
    # test __setitem__ with existing key
    table['banana'] = 8
   
    # verify that value was updated
    assert table['banana'] == 8
    
    # test __contains__ with existing and non-existing keys
    assert 'apple' in table
    assert 'banana' in table
    assert 'cherry' in table
    assert 'durian' not in table
    
    # test KeyError when getting non-existing key
    try:
        table['durian']
    except KeyError:
        pass
    else:
        assert False, 'KeyError not raised'
    
    # test exception when setting key in full table
    try:
        for i in range(10):
            table[str(i)] = i
    except Exception:
        pass
    else:
        assert False, 'Exception not raised'
    
    print('All tests passed')

test_hash_table()