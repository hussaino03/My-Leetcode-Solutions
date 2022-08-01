class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return reduce(lambda a,b:(s:=max(a[0],a[2].get(b[1],0)),max(a[1],b[0]-s+1),{**a[2],b[1]:b[0]+1}),enumerate(s),(0,0,{}))[1]