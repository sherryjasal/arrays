def diagonalDifference(arr):
    right_sum = 0
    left_sum = 0
    for i in range(0, n):
        for j in range(0, n):
            if (i==j):
                left_sum += arr[i][j]
            if (i == n - j -1):
                right_sum += arr[i][j]
    return abs(left_sum - right_sum)
