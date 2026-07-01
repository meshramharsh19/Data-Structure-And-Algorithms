nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

non_rotating_array = nums[:-k]
rotating_array = nums[-k:]

nums = rotating_array + non_rotating_array

print(nums)