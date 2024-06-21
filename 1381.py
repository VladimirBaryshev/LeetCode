# 1381. Design a Stack With Increment Operation
# https://leetcode.com/problems/design-a-stack-with-increment-operation/description/


class CustomStack:

    def __init__(self, maxSize: int):
    
        self.stack = []
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
    
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        
      
    def pop(self) -> int:
    
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1
        

    def increment(self, k: int, val: int) -> None:
        
        # n = min(k, len(stack))
        for i in range(k):
            if i < len(self.stack):
                self.stack[i] += val


