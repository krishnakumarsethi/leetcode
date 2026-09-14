class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        memory = set()
        for right in range(len(s)):
            while s[right] in memory:
                memory.remove(s[left])
                left+=1
            memory.add(s[right])
            current_length = right - left + 1
            max_length = max(max_length,current_length)
        return max_length