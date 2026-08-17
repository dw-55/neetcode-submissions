class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]
        n = len(tokens)
        for i in range(n):
            if tokens[i] in operations:
                second = int(stack.pop())
                first = int(stack.pop())
                if tokens[i] == "+":
                    add = first+second
                    stack.append(add)
                if tokens[i] == "-":
                    subtract = first-second
                    stack.append(subtract)
                if tokens[i] == "*":
                    multiple = first*second
                    stack.append(multiple)
                if tokens[i] == "/":
                    divide = first/second
                    stack.append(int(divide))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
        