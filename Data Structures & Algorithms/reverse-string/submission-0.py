class Solution:
    def reverseString(self, s: List[str]) -> None:
        lmao = []
        for i in range(len(s)-1,-1,-1):
            lmao.append(s[i])
        for i in range(0,len(s)):
            s[i] = lmao[i]

        