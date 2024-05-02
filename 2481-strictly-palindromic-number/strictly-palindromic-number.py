class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def is_palindrome(s):
            return s == s[::-1]

        for base in range(2, n - 1):
            # Convert n to string representation in base 'base'
            num_in_base = self.convert_to_base(n, base)
            # Check if the string representation is a palindrome
            if not is_palindrome(num_in_base):
                return False
        
        return True
    
    def convert_to_base(self, num, base):
        if num == 0:
            return "0"
        
        digits = []
        while num:
            digits.append(str(num % base))
            num //= base
        
        return "".join(digits[::-1])
