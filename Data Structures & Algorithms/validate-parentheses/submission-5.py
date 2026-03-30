class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closePar = {"}":"{", "]":"[", ")":"("}

        for c in s:
            if c in closePar:
                if stack and stack[-1] == closePar[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False 