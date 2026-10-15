class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If the character is already inside the current window, move the left pointer
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            
            # Update the latest index of the character
            char_map[s[right]] = right
            
            # Calculate maximum window size seen so far
            max_length = max(max_length, right - left + 1)
            
        return max_length