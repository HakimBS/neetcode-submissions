class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        messi = strs[0]
        ronaldo = 0
        while ronaldo < len(strs):
            while messi != "":
                if not strs[ronaldo].startswith(messi):
                    messi = messi[:-1]
                else:
                    ronaldo += 1
                    break
            if messi == "":
                return ""
                    

        return messi