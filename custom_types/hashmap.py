# hash map
# format :  self.buckets[[(key1, a), (key3, c)], [(key2, b)], [], [(key4, d), (key5, e), (key6, f)]]

from custom_types.chained_list import chained_list


class Hashmap:
    def __init__(self, size: int, buckets: list[list[tuple[str, chained_list]]] =[] ):
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
                final_list = chained_list()
                final_list.append(value.get("first_node"))
                dict_to_chained_list(value, final_list)
                print(final_list)
                return final_list
        return None
    
    def __str__(self):
        return str(self.buckets)
    
# the json deserializer can't do everything, and it certainly can't works with our custom chained_list
def dict_to_chained_list(dictionnary, final_list:chained_list):
    if dictionnary.get("next_node") != None :
        # it's big brain time
        final_list.append(dict_to_chained_list(dictionnary.get("next_node"), final_list))

# json exemple at this point :
# {'first_node': {'data': {'date': '2023-12-25T12:57:32.963000+00:00', 'content': '$hello', 'author': 'Fafacraft'}, 
# 'next_node': {'data': {'date': '2023-12-25T12:57:48.610000+00:00', 'content': '$hello', 'author': 'Fafacraft'}, 'next_node': None}}}
