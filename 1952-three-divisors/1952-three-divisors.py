class Solution:
    def isThree(self, n: int) -> bool:
        div = 0
        for i in range(1, n + 1):
            if int(n) % i == 0:
                div += 1
                
        return div == 3