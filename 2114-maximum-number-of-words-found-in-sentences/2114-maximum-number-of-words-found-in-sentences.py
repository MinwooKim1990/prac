class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        f={}
        for i in range(len(sentences)):
            f[i]=len(sentences[i].split())
        return max(f.values())
            