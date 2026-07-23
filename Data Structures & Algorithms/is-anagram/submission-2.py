class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # else:
        #     return sorted(s) == sorted(t)

        if len(s)!=len(t):
            return False

        sFrequency, tFrequency = {}, {}
        for index in range(len(s)):
            sChar, tChar = s[index], t[index]
            sFrequency[sChar]=sFrequency.get(sChar,0)+1
            tFrequency[tChar]=tFrequency.get(tChar,0)+1
        return sFrequency == tFrequency


        