class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if (c == '(') | (c == '{') | (c == '['):
                stack.append(c)
            elif (c == ')') | (c == '}') | (c == ']'):
                if len(stack) != 0:
                    top = stack.pop()
                    if top == '(' and c == ')':
                        continue
                    elif top == '{' and c == '}':
                        continue
                    elif top == '[' and c == ']':
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("]"))
