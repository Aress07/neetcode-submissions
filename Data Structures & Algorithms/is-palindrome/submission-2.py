class Solution:
    def isPalindrome(self, s: str) -> bool:
        asciiNb, asciiChar = range(48, 58), range(97, 123)

        t = ""
        s = s.lower()
        for c in s:
            if ord(c) in asciiNb or ord(c) in asciiChar:
                t += c
        return t == t[::-1]