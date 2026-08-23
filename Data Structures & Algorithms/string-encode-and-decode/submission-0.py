class Solution:

    def encode(self, strs: List[str]) -> str:
        ronaldo = ""
        for num in strs:
            ronaldo = ronaldo + str(len(num)) + "#" + num
        return ronaldo

    def decode(self, s: str) -> List[str]:
        messi =[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1
            j= i + length
            messi.append(s[i:j])
            i=j
        return messi




