import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == "-":
                stack.append(stack.pop(-2) - stack.pop())
            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                divided = stack.pop(-2) / stack.pop()
                if divided > 0:
                    divided = math.floor(divided)
                elif divided < 0:
                    divided = math.ceil(divided)
                else:
                    divided = 0
                stack.append(divided)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()
                
