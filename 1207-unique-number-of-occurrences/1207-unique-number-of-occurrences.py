from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = collections.Counter(arr).values()
        return len(arr) == len(set(arr))