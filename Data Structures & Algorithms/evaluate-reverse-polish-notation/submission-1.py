class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                if token == "+":
                    first = stack.pop()
                    second = stack.pop()
                    res = first + second
                    stack.append(res)
                elif token == "-":
                    first = stack.pop()
                    second = stack.pop()
                    res = second-first
                    stack.append(res)
                elif token == "*":
                    first = stack.pop()
                    second = stack.pop()
                    res = first * second
                    stack.append(res)
                else:
                    first = stack.pop()
                    second = stack.pop()
                    res = int(second/first)
                    stack.append(res)
        return stack[0]