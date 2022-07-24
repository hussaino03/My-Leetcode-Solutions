class Solution:
    def isValid(self, s: str) -> bool:
        d ={')': "(", "}": "{", "]": "["}
        stack = []
        for each_ch in s:
            if each_ch in d.values():
                stack.append(each_ch)
                
            elif each_ch in d.keys():
                if len(stack) == 0 or (stack.pop() != d[each_ch]):
                    return False
                
                
        return stack == []