class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    def __getitem__(self, key):
        hash_value = self.hash(key)
        while self.keys[hash_value] is not None:
            if self.keys[hash_value] == key:
                return self.values[hash_value]
            hash_value = (hash_value + 1) % self.size
        raise KeyError(f"Key '{key}' does not exist.")
        
    def __setitem__(self, key, value):
        if None not in self.keys:
            raise Exception("Hash table is full.")
        hash_value = self.hash(key)
        while self.keys[hash_value] is not None and self.keys[hash_value] != key:
            hash_value = (hash_value + 1) % self.size
        self.keys[hash_value] = key
        self.values[hash_value] = value
        
    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False
        
    def hash(self, key):
        # hash function of choice: simple remainder of the key by the table size
        return hash(key) % self.size
    
def hash_test():
    table = HashTable(5)
    table["apple"] = 1
    table["banana"] = 2
    table["cherry"] = 3
    assert table["apple"] == 1
    assert table["banana"] == 2
    assert table["cherry"] == 3


    assert "apple" in table
    assert "banana" in table
    assert "cherry" in table
    assert "orange" not in table

    table["apple"] = 4
    assert table["apple"] == 4


    try:
        table["banana"]
    except KeyError as e:
        assert str(e) == "Key '' does not exist."
    else:
        assert False, "Expected KeyError."
    

def test_hash_collision():
    table = HashTable(3)
    table["apple"] = 1
    table["banana"] = 2
    table["cherry"] = 3
    try:
        table["orange"] = 4
    except Exception as e:
        assert str(e) == "Hash table is full."
    else:
        assert False, "Expected Exception."


hash_test()
print(test_hash_collision())
