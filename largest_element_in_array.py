def largest(arr, n):
    arr.sort()
    largest_element = arr[n-1]
    return largest_element

##Another way
def largest(arr, n):
    return max (arr)
