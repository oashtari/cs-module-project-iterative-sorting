# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # iterate through array (represents sorted-unsorted boundary moving across array), find smallest element in unsorted portion
    # once found, swap it with element on right edge of sorted portion



    # for i in range(len(arr)):
    #     #index of boundary, as well as index we're going to swap smallest element with
    #     boundary = i

    #     # find smallest element in unsorteed portion
    #     smallest_value  = arr[boundary]
    #     smallest_index = boundary
    #     for unsorted_index in range(boundary, len(arr)):
    #         if arr[unsorted_index] < smallest_value:
    #             smallest_value = arr[unsorted_index]
    #             smallest_index = unsorted_index

    #     # 'smallest_index' is the smallest element in unsorted portion

    #     # once that's found, swap it with element on right edge
    #     arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]
    # return arr


    for i in range(0, len(arr)-1):
        # SECOND SOLUTION
        # cur_index = i 
        smallest_index = i 

        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
    
    return arr

    # # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
    #     # TO-DO: find next smallest element
    #     # (hint, can do in 3 loc)
    #     # Your code here


    #     # TO-DO: swap
    #     # Your code here

    # return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr) == 0:
        return arr
    if maximum is None:
        maximum = max(arr)

    buckets = [0 for i in range(maximum+1)]

    for value in arr:
        if value < 0:
            return "Error, negatives not allowed"
        buckets[value] =+1

    # now buckets arr now has distinct counts of each value

    output = []
    for index, count in enumerate(buckets):
        output.extend([index for i in range(count)])
        


    return output
