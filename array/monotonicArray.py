nums = [5,5]
monoInc = False
monoDec = False 

for i in range (len(nums)):
    j = i + 1
    if j == len(nums):
        break
    else :
        if i <= j:
            if nums[i] < nums[j]: # for mono increase 
                monoInc = True
            elif nums[i] > nums[j]:
                monoDec = True
            elif nums[i] == nums[j]:
                if monoDec == False or monoInc == False:
                    monoDec = True
                else :
                    pass
                    

if monoInc == True and monoDec == True :
    print(False)
else :
    print(True)
