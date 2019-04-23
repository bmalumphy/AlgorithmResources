class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        i = 0
        hashMap = {}
        for j in range(0, n):
            if(s[j] in hashMap):
                i = max(hashMap[s[j]], i)
            ans = max(ans, j-i+1)
            hashMap[s[j]] = j + 1
        return ans