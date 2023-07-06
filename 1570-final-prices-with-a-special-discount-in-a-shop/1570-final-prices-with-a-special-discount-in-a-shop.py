class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        answer = prices

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                answer[stack[-1]] = prices[stack[-1]] - prices[i]
                stack.pop()
            stack.append(i)
 
        return answer or prices

