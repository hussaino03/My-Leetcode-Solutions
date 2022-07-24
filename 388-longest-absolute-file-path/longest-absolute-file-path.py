class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        parts = input.split('\n')
        ans = 0
        stack = []
        L = 0
        for s in parts:
            cs = s.lstrip('\t')
            level = len(s) - len(cs)
            while stack and stack[-1][1] >= level:
                L -= len(stack.pop()[0])
            stack.append((cs, level))
            L += len(cs)
            if "." in cs:
                ans = max(ans, len(stack) + L - 1)                
        return ans
