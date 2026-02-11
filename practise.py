def prefix_sum(arr):
    prefix = [0]*len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = arr[i] + prefix[i-1]
    return prefix


