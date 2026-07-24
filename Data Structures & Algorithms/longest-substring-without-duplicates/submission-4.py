class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # The optimal sliding window
        lastseen={}
        left=0
        result=0
        for right in range(len(s)):
            if s[right] in lastseen:
                left=max(lastseen[s[right]]+1,left)
            lastseen[s[right]]=right
            result=max(result,right-left+1)
        return result
        