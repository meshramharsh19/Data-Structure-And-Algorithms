class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        freq = {}

        for num in nums:
            compliment = k - num

            # compliment exists → pair mil gaya
            if compliment in freq and freq[compliment] > 0:
                operations += 1
                freq[compliment] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1

        return operations

        