# leetcode hard

def minPatches(nums, n):
    # Ye brute force approach hai
    
    # Poora array dekhne ke liye
    reached = set()  # Jo numbers ban gaye unhe store karo
    
    # Har ek subset (combination) ke liye
    for i in range(len(nums)):
        new_reached = set()
        new_reached.add(nums[i])  # Single element
        
        # Pichle sare combinations mein add karo
        for num in reached:
            new_reached.add(num + nums[i])
        
        reached.update(new_reached)
    
    # Ab dekhte hain kaun se numbers missing hain
    patches = 0
    for i in range(1, n + 1):
        if i not in reached:
            patches += 1
            # Patch add karte hain
            for num in list(reached):
                reached.add(num + i)
            reached.add(i)
    
    return patches

# Example
nums = [1, 3]
n = 6
print(minPatches(nums, n))  # Output: 1

nums = [1,3]
n = 6
reached = set() 
print(reached)
for i in range(len(nums)):
    new_reached = set()
    new_reached.add(nums[i]) 
    print("first loop", new_reached)
    for num in reached:
        new_reached.add(num + nums[i]) 
        
    reached.update(new_reached)
    print("second loop", new_reached)
    

print("---------------------------")
print(reached)
