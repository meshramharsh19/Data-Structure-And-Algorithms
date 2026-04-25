class Solution:
    def compress(self, chars: List[str]) -> int:
        S = []
        count = 1

        # Main loop (till second last index)
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                count += 1
            else:
                # Add character
                S.append(chars[i])
                # Add count if > 1
                if count > 1:
                    for digit in str(count):
                        S.append(digit)
                count = 1
        
        # Handle last character group
        S.append(chars[-1])
        if count > 1:
            for digit in str(count):
                S.append(digit)

        # Overwrite original array
        chars[:] = S

        return len(chars)
