class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for num in s:
            if num == "(" or num == "{" or num == "[":
                stack.append(num)
            else:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if num == ")" and top != "(":
                        return False
                    if num == "]" and top != "[":
                        return False
                    if num == "}" and top != "{":
                        return False
        return len(stack) == 0