"""
 You are given an array of integer, delete the the duplicate 
 integer from the array and array should be sorted
"""

def delete_duplicate(arr):
    # Sorting the array in ascending order
    print('Unsorted list:', arr)
    arr.sort()
    print('Sorted list:', arr)

    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i+1]:
            del arr[i]
        else:
            i += 1

    print('Final list after duplicate deletion:', arr)

print(delete_duplicate([4,2,3,4,5,6,7]))   # [2,3,4,5,6,7]
