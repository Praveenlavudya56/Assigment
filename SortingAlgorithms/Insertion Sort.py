def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)
#--------------------------------------------------------------------------
def insertionSort(arr,l):
    for i in range(1,l):
        currentElement  = arr[i]
        j = i-1

        while j>=0 and arr[j]>currentElement:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = currentElement

    return arr


arr = [5,1,9,4,2]
l = len(arr)
print(insertionSort(arr,l))
