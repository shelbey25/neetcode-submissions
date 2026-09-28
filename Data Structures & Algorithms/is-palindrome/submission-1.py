class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            while not s[left].isalnum():
                left+=1
                if left >= len(s):
                    return True
            while not s[right].isalnum():
                right-=1
                if right < 0:
                    return True
            if s[left].lower() != s[right].lower():
                return False
            right-=1
            left+=1

        return True