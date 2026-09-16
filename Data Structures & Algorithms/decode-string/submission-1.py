class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nums = '0123456789'
        alp = 'abcdefghijklmnopqrstuvwxyz'
        for c in s:
            if c in nums:
                if stack and stack[-1][0] in nums:
                    num = stack.pop(-1)
                    # print(num, num+c)
                    stack.append(num+c)
                else:
                    stack.append(c)
            elif c in alp:
                if stack and stack[-1][0] in alp:
                    char = stack.pop(-1)
                    # print(char, char+c)
                    stack.append(char+c)
                else:
                    stack.append(c)
            elif c == ']':
                char, obs, num = stack.pop(), stack.pop(), int(stack.pop())
                # print(char, num)
                tmp = char*num
                if stack and stack[-1][0] in alp:
                    ch = stack.pop(-1)
                    # print(ch, ch+tmp)
                    stack.append(ch+tmp)
                else:
                    stack.append(tmp)
            else:
                stack.append(c)
                # stack.append(char+num)
        return stack[-1]