class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(['a', 'i', 'e', 'o', 'u'])
        count = 0
        for i in range(k):
            if s[i] in vowel:
                count += 1
        maxcount = count

        for i in range (k, len(s)):
            if s[i] in vowel:
                count += 1
            if s[i-k] in vowel:
                count -= 1
            if count > maxcount:
                maxcount = count 
        return maxcount

        