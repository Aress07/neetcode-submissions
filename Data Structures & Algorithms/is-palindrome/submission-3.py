class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        letters = range(97, 123)
        numbers = range(48, 58)

        t = ""
        for char in s:
            if ord(char) in letters or ord(char) in numbers:
                t += char

        return t == t[::-1]

