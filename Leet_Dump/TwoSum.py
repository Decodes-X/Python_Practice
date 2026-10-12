nums = [-10,7,19,15] 
target = 9 #9
over = {} 

for i, num in enumerate(nums):
    newAns = target - num
    if newAns in over:
        print([over[newAns], i])
    over[num] = i