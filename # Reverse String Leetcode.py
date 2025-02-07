# 344. Reverse String Leetcode

class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1  

        while left < right:
            s[left], s[right] = s[right], s[left]  
            left += 1
            right -= 1
sol = Solution()
s = ["h", "e", "l", "l", "o"]
sol.reverseString(s)
print(s)