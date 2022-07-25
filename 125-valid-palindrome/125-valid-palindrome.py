import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "")
        s = s.lower()
        return s == s[::-1]
