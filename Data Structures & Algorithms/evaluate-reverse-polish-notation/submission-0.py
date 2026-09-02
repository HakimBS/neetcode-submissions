class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        messi = []
        sum = 0
        for num in tokens:
            if num not in {"+", "-", "*", "/"}:
                messi.append(int(num))
            else:
                b = messi.pop()
                a = messi.pop()
                if num == "+":
                    messi.append(a+b)
                elif num == "-":
                    messi.append(a-b)
                elif num == "*":
                    messi.append(a*b)
                elif num == "/":
                    messi.append(int(a/b))
        return messi[0]

                


        