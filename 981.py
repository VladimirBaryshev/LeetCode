# "TimeMap" [] --> null
# "set" ["foo", "bar", 1] --> null
# "get" ["foo", 1] --> "bar"
# "get" ["foo", 3] --> "bar"
# "set" ["foo", "bar2", 4] --> null
# "get" ["foo", 4] --> "bar2"
# "get" ["foo", 5] --> "bar2"


class TimeMap:

    def __init__(self):

        self.keyStore = dict()


    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.keyStore:
            self.keyStore[key] = list()

        self.keyStore[key].append(tuple((value, timestamp)))


    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        values = self.keyStore.get(key, [])

        l = 0
        r = len(values) - 1

        while l <= r:

            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res



# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1) # --> null
obj.get("foo", 1) # --> "bar"
obj.get("foo", 3) # --> "bar"
obj.set("foo", "bar2", 4) # --> null
obj.get("foo", 4) # --> "bar2"
obj.get("foo", 5) # --> "bar2"
