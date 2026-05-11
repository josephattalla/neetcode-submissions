class Solution:
    def isPalindrome(self, s: str) -> bool:
        lptr = 0
        rptr = len(s) - 1 

        while lptr < rptr and rptr > 0 and lptr < len(s):
            while not s[lptr].isalnum() and lptr < rptr:
                lptr += 1
            while not s[rptr].isalnum() and rptr > lptr:
                rptr -= 1
            
            if s[lptr].lower() != s[rptr].lower() and lptr < rptr:
                return False
            
            lptr += 1
            rptr -= 1
        
        return True