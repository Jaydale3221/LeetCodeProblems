class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popInd = 0 


        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[popInd]:
                stack.pop()
                popInd += 1
            
        return not stack