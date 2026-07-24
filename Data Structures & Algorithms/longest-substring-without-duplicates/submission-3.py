class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #The sliding window solution
        charSet=set()
        left=0
        result=0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            result=max(result, right-left+1) # removed the dependency on the length of the set instead calculating the window size
        return result
        