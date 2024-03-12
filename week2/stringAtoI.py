#URL: https://leetcode.com/problems/string-to-integer-atoi/
# Description: Implement atoi which converts a string to an integer.

# Input: s = "42"
# Output: 42

# Input: s = "   -42"
# Output: -42

'''
Approach:
1. We use a while loop to iterate through the string.
2. We ignore the leading spaces.
3. We check for the sign of the number.
4. We iterate through the string and check if the character is a number.
5. We keep adding the number to a temporary string.
6. We return the number after checking for the sign.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        flag = 0
        sign = 1
        l = len(s)
        temp = ""
        while(i<l and s[i]==" "):
            i=i+1
        if i==l:
            return 0
        if(s[i]=="-"):
            sign = -1
            i+=1
        elif(s[i]=="+"):
            i+=1
        
        while(flag!=1 and i<l):
            if(s[i].isnumeric()):
                temp = temp+s[i]
            else:
                flag=1
            i+=1
        if(len(temp)==0):
            return 0
        if(sign==1):
            return min(2**31 - 1, int(temp)*sign)
        return max((-2)**31, int(temp)*sign)