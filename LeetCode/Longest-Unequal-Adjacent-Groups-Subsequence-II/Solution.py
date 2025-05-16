class Solution:
    def getWordsInLongestSubsequence(self, w: List[str], g: List[int]) -> List[str]:
        def hamming1(a, b):
            if len(a) != len(b):
                return False
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
        
        n = len(w)
        dp = [1] * n
        prev = [-1] * n
        max_len = 1
        max_idx = 0    
        for i in range(n):
            for j in range(i):
                if g[i] != g[j] and hamming1(w[i], w[j]):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        seq = []
        cur = max_idx
        while cur != -1:
            seq.append(w[cur])
            cur = prev[cur]
        seq.reverse()
        return seq