class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        b=a[::-1]
        if str(x)==b:
            return True
        else:
            return False
        
