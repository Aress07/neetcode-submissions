class Solution:

    def encode(self, strs: List[str]) -> str:
        special = "#"
        ret = ""
        for s in strs:
            ret += str(len(s)) + special + s
        return ret

    def decode(self, s: str) -> List[str]:
        num = ""
        arr = []
        i = 0
        while i < len(s):
            if s[i] != "#":
                num += s[i]
                i += 1
            else:
                num = int(num)
                arr.append(s[i+1:i+1+num])
                i = i + 1 + num
                num = ""
        return arr

            