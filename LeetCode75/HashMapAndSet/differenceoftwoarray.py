

nums11 = [1,2,3,3]
nums22 = [1,1,2,2]


nums1 = set(nums11)
nums2 = set(nums22)

ans1 = nums1 - nums2
ans2 = nums2 - nums1
ans = list((list(ans1), list(ans2)))
print(ans)