class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hashMap:
                hashMap[key].append(s)
            else:
                hashMap[key] = [s]
        return list(hashMap.values())