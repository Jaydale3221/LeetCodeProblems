class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]* len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() #stackT is temperature and stackInd is Index
                result[stackInd] = (i - stackInd)
            stack.append([t,i])
        return result