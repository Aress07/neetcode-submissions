class Solution:
    def isPalindrome(self, s: str) -> bool:
        asciiMin, asciiDig = range(97, 123), range(48, 58)
        s = s.lower()
        t = ""
        for c in s:
            if ord(c) in asciiMin or ord(c) in asciiDig: t += c

        return t == t[::-1]
