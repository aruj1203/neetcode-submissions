class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        i=""
        for ch in s:
            if ch.isalnum():
                i+=ch
        return i==i[::-1]