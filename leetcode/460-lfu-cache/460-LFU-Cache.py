import collections

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_val = {}
        self.key_freq = {}
        self.freq_keys = collections.defaultdict(collections.OrderedDict)

    def _update_frequency(self, key: int):
        freq = self.key_freq[key]

        del self.freq_keys[freq][key]

        if not self.freq_keys[freq] and self.min_freq == freq:
            self.min_freq += 1

        self.key_freq[key] = freq + 1
        self.freq_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
            
        self._update_frequency(key)
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_val:
            self.key_val[key] = value
            self._update_frequency(key)
        else:
            if len(self.key_val) >= self.capacity:
                evict_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
                del self.key_val[evict_key]
                del self.key_freq[evict_key]

            self.key_val[key] = value
            self.key_freq[key] = 1
            self.freq_keys[1][key] = None
            self.min_freq = 1