# 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/description/



class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.cur = 0


    def visit(self, url: str) -> None:
    
        while len(self.stack)-1 > self.cur:
            self.stack.pop()
        self.stack.append(url)
        self.cur += 1
        

    def back(self, steps: int) -> str:
        if self.cur - steps < 0:
            self.cur = 0
            return self.stack[0]
        else:
            self.cur -= steps
            return self.stack[self.cur]
    
        

    def forward(self, steps: int) -> str:

        if self.cur + steps >= len(self.stack):
            self.cur = len(self.stack)-1
            return self.stack[-1]
        else:
            self.cur += steps
            return self.stack[self.cur]
           
