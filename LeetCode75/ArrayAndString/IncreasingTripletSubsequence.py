class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_value = float("inf")
        sec_value = float("inf")
        for nums in nums:
            if nums <= min_value:
                min_value = nums
                print(min_value)
            elif nums <= sec_value:
                sec_value = nums
                print(sec_value)
            else:
                return True
        else:
            return False