class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # print(stack, t)
            if t in "+-*/":
                x = stack.pop()
                y = stack.pop()
                if t == "+":
                    t = x + y
                elif t == "-":
                    t = y-x
                elif t == "*":
                    t = y*x
                else:
                    t = int(y/x)
            stack.append(int(t))
        return stack[0]