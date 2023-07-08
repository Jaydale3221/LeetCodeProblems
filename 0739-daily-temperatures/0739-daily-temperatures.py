class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        deque = collections.deque()
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while deque and temperatures[deque[-1]] < temperatures[i]:
                j = deque.pop()
                answer[j] = i - j
            deque.append(i)
        
        return answer


      