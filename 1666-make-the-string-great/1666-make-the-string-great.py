class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if i == 0 :
                stack.append(s[i])
            elif stack and s[i] != stack[-1]:
                if s[i].lower() == stack[-1].lower():
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        return "".join(stack) if stack else ""

    