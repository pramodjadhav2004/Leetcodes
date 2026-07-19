#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_num=str(x)
        rev=str_num[::-1]
        if str_num==rev:
            return True
        else:
            return False
try:
    num = int(user_input)
    solution = Solution()
    result = solution.isPalindrome(num)
    print(f"Is {num} a palindrome? {result}")
    
except ValueError:
    print("Please enter a valid integer.")