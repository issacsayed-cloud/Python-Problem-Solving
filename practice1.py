def has_subarray_sum(arr, K):
    prefix_sum = 0
    seen = set()
    seen.add(0)  # handles subarray starting at index 0

    for x in arr:
        prefix_sum += x
        if prefix_sum - K in seen:
            return True
        seen.add(prefix_sum)

    return False


arr = [3, 5, 2, 7, 1, 4]
K = 10
print(has_subarray_sum(arr, K))  # Output → True


