# hash map
# format :  self.buckets[[(key1, a), (key3, c)], [(key2, b)], [], [(key4, d), (key5, e), (key6, f)]]
from json import JSONEncoder


class Hashmap:
    def __init__(self, size, buckets = []):
        self.size = size
        self.buckets = buckets
        for _ in range(size):
            self.buckets.append([])

    def set(self, key, value):
        bucket = self.buckets[hash(key) % self.size]
        # overwrite to avoid doubles of the same keys
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
        self.buckets[hash(key) % self.size].append((key, value))

    def get(self, key):
        for k,value in self.buckets[hash(key) % self.size]:
            if k == key:
                return value
        return None
    
    def __str__(self):
        return str(self.buckets)
    

class HashmapJSONEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__
