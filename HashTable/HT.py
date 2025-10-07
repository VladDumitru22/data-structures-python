class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key, value):
        idx = self.__hash(key)
        if self.data_map[idx] is None:
            self.data_map[idx] = []
        self.data_map[idx].append([key, value])
    
    def get_item(self, key):
        idx = self.__hash(key)
        if self.data_map[idx] is not None:
            for i in range(len(self.data_map[idx])):
                if self.data_map[idx][i][0] == key:
                    return self.data_map[idx][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
hash_table = HashTable()

hash_table.set_item('bolts', 1400)
hash_table.set_item('washers', 50)
hash_table.set_item('lumber', 70)

hash_table.print_table()

print(hash_table.get_item('lumber'))

print(hash_table.keys())