class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        reversed_list = s[::-1]
        reverse_statement = ' '.join(reversed_list)
        return reverse_statement