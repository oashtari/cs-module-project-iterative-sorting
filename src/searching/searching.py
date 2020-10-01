def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        # print('arr i', i)
        if arr[i] == target:
            return i
        
    return -1   # not found



# Write an iterative implementation of Binary Search
# Returns either the index of the target in the arr or if the target isn't in the arr, return -1

def binary_search(arr, target):
    #1 compare target element to midpoint
        # how do we find midpoint, what do we need to know
        # lenght of arr would help
        # the 'range': if we have left-most index and right-most index
        # then midpoint is floor((right index - left index) / 2)
    #2 determine which half to go in, toss out other half
        # reassign either left or right index to point to element past midpoint

    #3 if midpoint matches target, then we've found it and reutrn midpoint index
    #4 repeat process, we need to loop this
        #what's our looping criteria to let us know we're done looping
        # if we see that low and high are same index, 
        # and element is not target, can conclude element is not in array
        # when low and high meet, that's when we stop looping
    
    low = 0
    high = len(arr) - 1

    while low <= high:
        
        mid = (high + low ) // 2 # double slack automatically floors the result
        if target == arr[mid]:
            return mid

        if target < arr[mid]: #cut out right half, reassign hight to mid-1
            high = mid -1
        
        if target > arr[mid]:
            low = mid +1



    return -1  # not found
