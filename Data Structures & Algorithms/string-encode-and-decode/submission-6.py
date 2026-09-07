class Solution:

    def encode(self, strs: List[str]) -> str:
        # Hello Wo@rld > @5Hello@5World
        enc_char = '@'
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + enc_char + s
        return encoded
    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World 7
        list_ = []
        num = ""
        i = 0

        while i < len(s):
            if s[i] != '@':
                num += s[i]
                i += 1
            else:
                num = int(num)
                list_.append(s[i + 1: i + 1 + num])
                i = i + 1 + num
                num = ""
        return list_