# 706. Design HashMap

class MyHashMap:

    def __init__(self):
        
        self.h_map = [None for i in range(0, (10**6)+1)]
        

    def put(self, key: int, value: int) -> None:
        
        self.h_map[key] = value


    def get(self, key: int) -> int:
        
        if self.h_map[key] == None:
            return -1
        return self.h_map[key]


    def remove(self, key: int) -> None:
        
        self.h_map[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.get(3))
print(obj.put(2,1))
print(obj.get(2))
print(obj.remove(2))
print(obj.get(2))


# # Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

