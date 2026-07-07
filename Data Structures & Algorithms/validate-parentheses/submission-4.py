class Solution:
    def isValid(self, s: str) -> bool:
        '([{}([])()])'

        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                return False

        if not stack:
            return True
        else:
            return False