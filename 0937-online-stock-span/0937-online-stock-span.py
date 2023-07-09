class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        answer = 1 #counting self

        while self.stack and self.stack[-1][0] <= price:
            # print(self.stack.pop()[1])
            answer += self.stack.pop()[1]
        self.stack.append([price,answer])
        # print(price, answer)
        return answer
        
        
