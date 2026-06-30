class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using a hashMap
        
        if len(t) != len(s): return False

        hmS = {}
        hmT = {}

        for i, j in zip(s, t):
            hmS[i] = hmS.get(i, 0) + 1 
            hmT[j] = hmT.get(j, 0) + 1

        return hmS == hmT