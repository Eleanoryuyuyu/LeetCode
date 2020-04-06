class LFUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        from collections import defaultdict
        self.cache = {}
        self.visited = {}
        self.key_list = defaultdict(OrderedDict)
        self.capacity = capacity
        self.mincount = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        count = self.visited[key]
        self.visited[key] += 1
        self.key_list[count].pop(key)
        self.key_list[count + 1][key] = None

        if count == self.mincount and len(self.key_list[count]) == 0:
            self.mincount += 1
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return
        else:
            if len(self.cache) == self.capacity:
                tmp_k, tmp_v = self.key_list[self.mincount].popitem(last=False)
                del self.cache[tmp_k]
                del self.visited[tmp_k]

        self.cache[key] = value
        self.visited[key] = 1
        self.key_list[1][key] = None
        self.mincount = 1




# Your LFUCache object will be instantiated and called as such:
cache = LFUCache(3)
cache.put(2, 2)
cache.put(1, 1)
print(cache.get(2))
print(cache.get(1))
print(cache.get(2))
cache.put(3,3)
cache.put(4,4)
print(cache.get(3))
print(cache.get(2))
print(cache.get(1))
print(cache.get(4))


