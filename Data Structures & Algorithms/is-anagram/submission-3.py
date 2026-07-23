class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        sFrequency, tFrequency={},{}
        
        for i in range(len(s)):
            sChar=s[i]
            tChar=t[i]

            sFrequency[sChar]=sFrequency.get(sChar,0)+1
            tFrequency[tChar]=tFrequency.get(tChar,0)+1

        return sFrequency == tFrequency