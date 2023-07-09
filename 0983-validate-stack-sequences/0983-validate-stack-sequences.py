class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0

        for right in pushed:
            stack.append(right)

            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1

        return True if not stack else False
            
