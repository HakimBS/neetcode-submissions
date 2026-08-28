class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lmao = { ")" : "(", "]" : "[", "}" : "{" }
        for num in s:
            if num in lmao:
                if not stack:
                    return False
                messi = stack.pop()
                if messi != lmao[num]:
                    return False
            else:
                stack.append(num)
        return len(stack) == 0