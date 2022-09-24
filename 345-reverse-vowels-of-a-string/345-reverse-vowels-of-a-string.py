class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        start = 0
        end = len(s)-1
        
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        s = list(s)
        
        while start < end:
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                end-=1
                start+=1
                continue
                
            if s[end] not in vowels:
                end-=1
            if s[start] not in vowels:
                start +=1
                
        return ''.join(s)
            