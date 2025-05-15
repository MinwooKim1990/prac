class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans=[words[0]]
        for i in range(len(groups)-1):
            if groups[i+1] != groups[i]:
                ans.append(words[i+1])
        return ans