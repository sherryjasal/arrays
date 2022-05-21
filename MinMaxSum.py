#the minimum sum and the maximum sum of 4 of 5 elements.
### sort the array first ###
### check for pattern ###

def miniMaxSum(arr):
    arr.sort()
    total = sum(arr)        
    max_val = total - arr[0]
    min_val = total - arr[len(arr)-1]
    print (min_val , max_val)
