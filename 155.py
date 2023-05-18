# 155. Min Stack
# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.stack = list()
        self.stack_min = list()

    def push(self, val: int) -> None:

        self.stack.append(val)
        
        if self.stack_min:
            val = min(val, self.stack_min[-1])
        self.stack_min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]

# # [[],[-2],[0],[-3],[],[],[],[]]
# # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.getMin()) # -3
# obj.pop() 
# print(obj.top()) # 0
# print(obj.getMin()) # -2


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)
print(obj.getMin()) # -2
print(obj.top()) # -1
obj.pop()
print(obj.getMin()) # -2



