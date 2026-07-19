from math import sqrt

class Solution(object):
    def mySqrt(self, x):
        return int(sqrt(x))

x = int(input())
solution = Solution()
print(solution.mySqrt(x))