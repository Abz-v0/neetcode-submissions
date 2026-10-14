class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o_br = ["(", "{", "["]
        c_br = [")", "}", "]"]

        for c in s:
            if c in o_br:
                stack.append(c)
            elif c in c_br:
                if not stack:
                    return False

                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack