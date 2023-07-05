def max_increasing_subarray_length(n, nums):
    
    # max_length stores the maximum length of increasing subarray
    # current_length stores the length of the current increasing subarray
    maximum_length = 1
    current_length = 1
    
    # Iterate through the elements of the array
    for i in range(1, n):
        # If the current element is greater than the previous one,
        # it can be included in the current increasing subarray
        if nums[i] > nums[i-1]:
            current_length += 1
            maximum_length = max(maximum_length, current_length)
        # Otherwise, start a new increasing subarray
        else:
            current_length = 1
            
    return maximum_length

# Example usage:

# Read the number of elements
n = int(input())

# Read the elements of the array
arr = list(map(int, input().split()))

# Find and print the maximum length of an increasing subarray
print(max_increasing_subarray_length(n, arr))