class Solution:

    def encode(self, strs: List[str]) -> str:
        special = "@"
        ret = ""
        for s in strs:
            ret += str(len(s)) + special + s
        return ret
    def decode(self, s: str) -> List[str]:
        list_ = []
        number = ""
        i = 0
        while i < len(s):
            if s[i] != "@":
                number += s[i]
                i += 1
            else:
                n = int(number)
                list_.append(s[i+1: i+1+n])
                i = i+1+n
                number = ""
        return list_