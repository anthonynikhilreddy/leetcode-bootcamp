# URL: https://leetcode.com/problems/longest-repeating-character-replacement/
# 424. Longest Repeating Character Replacement

# Input: s = "ABAB", k = 2
# Output: 4

# Input: s = "AABABBA", k = 1
# Output: 4

'''
Approach:
1. We use the sliding window approach.
2. We keep a count of the characters in the window.
3. We check if the maximum count of the characters in the window is less than or equal to k.
4. If it is, we update the maximum length of the window.
5. If not, we move the left pointer of the window and update the count of the character at the left pointer.

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        temp = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            temp_len = r-l+1
            if(temp_len - max(count.values()) <= k):
                temp = max(temp, temp_len)
            else:
                count[s[l]] = count[s[l]]-1
                l = l+1
        return temp