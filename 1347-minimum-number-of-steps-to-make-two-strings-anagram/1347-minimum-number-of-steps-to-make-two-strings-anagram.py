from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Use Counter to get character counts for both strings in a single pass
        s_count = Counter(s)
        t_count = Counter(t)
        
        steps = 0
        # Calculate steps needed by comparing character counts in s to those in t
        for char, count in s_count.items():
            steps += max(count - t_count.get(char, 0), 0)
        
        return steps