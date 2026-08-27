class Solution:
    def calPoints(self, operations: List[str]) -> int:
        messi = []
        lmao=0
        for num in operations:
            if num == "+":
                messi.append(messi[-1]+messi[-2])
            elif num == "C":
                messi.pop()
            elif num == "D":
                messi.append(messi[-1]*2)
            else:
                messi.append(int(num))
        lmao = sum(messi)
        return lmao
        