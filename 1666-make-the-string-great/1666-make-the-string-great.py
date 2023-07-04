class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  # Initialize an empty stack to keep track of characters in the modified string

        for i in range(len(s)):  # Iterate through each character in the input string
            if i == 0:
                stack.append(s[i])  # For the first character, directly append it to the stack
            elif stack and s[i] != stack[-1]:
                # If stack is not empty and current character is different from the top character of the stack
                if s[i].lower() == stack[-1].lower():
                    stack.pop()  # Remove the top character from the stack if it forms a "bad" pair with the current character
                else:
                    stack.append(s[i])  # Append the current character to the stack
            else:
                stack.append(s[i])  # If current character is the same as the top character of the stack, append it to the stack

        return "".join(stack) if stack else ""  # Join the characters in the stack to form the modified string, or return an empty string if the stack is empty
