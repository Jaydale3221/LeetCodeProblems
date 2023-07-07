class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': True,
            '-': True,
            '/': True,
            '*': True
            }

        for num in tokens:
            if num not in operators:
                stack.append(int(num))
            else:
                right  = int(stack.pop())
                left = int(stack.pop())
                # print(left, right, num)
                if num == '+':
                    stack.append(left + right)
                elif num == '-':
                    stack.append(left - right)
                elif num == '/':
                    stack.append(int(left / right))
                elif num == '*':
                    stack.append(left * right)
        return stack[0]