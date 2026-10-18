from collections import defaultdict
from bisect import bisect_left, bisect_right

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        key_list = self.map[key]

        i = bisect_left(
            key_list,
            timestamp,
            key=lambda item: item[0]
        )

        # this logic handles the replacement case if one sets same timestamp again
        # and the policy is to replace the value of the timestamp
        if i < len(key_list) and key_list[i][0] == timestamp: 
            key_list[i] = (timestamp, value)
        else:
            key_list.insert(i, (timestamp, value))

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