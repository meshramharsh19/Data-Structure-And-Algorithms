class Solution:
    def reverseVowels(self, s: str) -> str:
        L = list(s)
        orignal_vowel_format = []
        orignal_cons_format = []
        position_of_vowel = []
        vowel = 'aeiouAEIOU'
        for i in range (len(L)):
            if L[i] in vowel:
                orignal_vowel_format.append(L[i])
                position_of_vowel.append(i)
            else:
                orignal_cons_format.append(L[i])
            
        orignal_str = ''.join(orignal_vowel_format)
        reversed_str = orignal_str[::-1]
        reversed_format = list(reversed_str)
        for i in range (len(reversed_format)):
            orignal_cons_format.insert(position_of_vowel[i],reversed_format[i])

        orignal_str = ''.join(orignal_cons_format)
        return orignal_str
