class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.strip()
        strList = stripped.split(" ")
        #return strList
        lastWord = strList[-1]
        return len(lastWord)
        
