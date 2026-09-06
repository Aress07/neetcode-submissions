class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_S(s): return "".join(sorted(s))
        hashMap = defaultdict(list)
        for s in strs:
            hashMap[sort_S(s)].append(s)

        return list(hashMap.values())