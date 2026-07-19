#Given a string s consisting of words and spaces, return the length of the last word in the string.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = s.strip().split()
        return len(s1[-1])

s = input("Enter a string: ")
solution = Solution()
result = solution.lengthOfLastWord(s)
print("Length of the last word:", result)