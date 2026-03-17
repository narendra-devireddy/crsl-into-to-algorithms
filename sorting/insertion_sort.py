# Insertion Sort Algorithm
# Pick the current element and compare it with the elements before it.
#  If the current element is smaller than the compared element, 
#   shift the compared element one position to the right. 
#   Repeat this process until you find the correct position for the current element 
#       and insert it there.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, -1, -8, 0]
    print("Original array:", arr)
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)