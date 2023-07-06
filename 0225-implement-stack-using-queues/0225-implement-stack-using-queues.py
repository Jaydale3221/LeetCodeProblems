class MyStack:

    def __init__(self):
        self.main = collections.deque()

    def push(self, x: int) -> None:
        self.main.append(x)
        

    def pop(self) -> int:
        second = collections.deque()
        while len(self.main) > 1:
            second.append(self.main.popleft())
        top = self.main.popleft()
        self.main = second
        return top
        # while len(self.main) > 1:
        #     second.append(self.main.popleft())
        # top = self.main.popleft()
        # self.main = second
        # return top
        
    def top(self) -> int:
        return self.main[-1]


        

    def empty(self) -> bool:
        return not self.main
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()