class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        left = 0

        for right in pushed:
            stack.append(right)


            while stack and stack[-1] == popped[left]:
                stack.pop()
                left += 1
        
        return  not stack
            
