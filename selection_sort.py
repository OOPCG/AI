def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Assume the minimum element is at the current position
        min_index = i
        
        # Find the actual minimum element in the unsorted part
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example Usage
arr = [64, 25, 12, 22, 11]

print("Original array:")
print(arr)

selection_sort(arr)

print("Sorted array:")
print(arr)
