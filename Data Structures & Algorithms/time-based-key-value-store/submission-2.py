from collections import defaultdict
from bisect import bisect_left, bisect_right

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        key_list = self.map[key]
        item = (timestamp, value)
        key_list.append(item)
        #key_list.insert(bisect_right(key_list, item), item)

    def get(self, key: str, timestamp: int) -> str:
        key_list = self.map[key]
        # if not key_list:
        #     return ""
        
        index = bisect_right(key_list, timestamp, key=lambda item: item[0]) - 1
        if index >= 0: # means an time <= timestamp DOES exist in list
            return key_list[index][1]
        else:
            return "" # doesn't exist in list

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)