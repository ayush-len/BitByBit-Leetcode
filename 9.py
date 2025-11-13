class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        z = "".join(reversed(y))
        if y == z:
            return True
        else:
            return False
