class Solution:
    def calPoints(self, operations: List[str]) -> int:
        messi = []
        lmao=0
        for num in operations:
            if num == "+":
                lmao += messi[-1] + messi[-2]
                messi.append(messi[-1]+messi[-2])
            elif num == "C":
                lmao -= messi[-1]
                messi.pop()
            elif num == "D":
                lmao += messi[-1]*2
                messi.append(messi[-1]*2)
            else:
                lmao += int(num)
                messi.append(int(num))
        return lmao
        