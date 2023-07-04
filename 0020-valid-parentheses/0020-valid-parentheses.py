class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')','{':'}','[':']'}
        

        for c in s: 
            if c in brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                temp = stack.pop()
                if c!= brackets[temp]:
                    return False
            
        return not stack
         