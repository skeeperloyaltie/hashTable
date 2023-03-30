class HashTableLP:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __setitem__(self, key, value):
        index = self.hash(key)

        while self.keys[index] is not None and self.keys[index] != key:
            index = (index + 1) % self.size

        if self.keys[index] == key:
            self.values[index] = value
        else:
            self.keys[index] = key
            self.values[index] = value

    def __getitem__(self, key):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size

        raise KeyError(f"Key '{key}' not found.")

    def __contains__(self, key):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.size

        return False

    def hash(self, key):
        # Our hash function
        return sum([ord(c) for c in key]) % self.size

def test_hash_table():
    table = HashTableLP(5)

    table['cat'] = 'meow'
    table['dog'] = 'woof'
    table['bird'] = 'tweet'

    assert table['cat'] == 'meow'
    assert table['dog'] == 'woof'
    assert table['bird'] == 'tweet'

    table['dog'] = 'bark'
    assert table['dog'] == 'bark'

    assert 'cat' in table
    assert 'dog' in table
    assert 'bird' in table

    assert 'lion' not in table
    assert 'elephant' not in table

    try:
        table['lion']
    except KeyError as e:
        assert str(e) == "Key 'lion' not found."
    else:
        assert False, "Expected KeyError for non-existent key."

    try:
        table['ant'] = 'crawl'
    except Exception as e:
        assert str(e) == "Hash table is full."
    else:
        assert False, "Expected exception for full hash table."

test_hash_table()

