# Delete root from -> [0, 40, 35, 30, 15, 10, 25, 5]


def delete(arr: list[int], length: int):
    # Step 1: Move last element to the start position
    arr[1], arr[length - 1] = arr[length - 1], arr[1]

    # Step 2: Swap with larger child until child is larger
    i = 1
    j = 2 * i
    n = length - 1  # Now heap size is less by
    while j < n - 1:
        if arr[j + 1] > arr[j]:
            j = j + 1
        if arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]
        else:
            break


heap = [0, 40, 35, 30, 15, 10, 25, 5]
length = len(heap)
delete(heap, length)
print("New heap => ", heap)


# Heap sort
heap = [0, 40, 35, 30, 15, 10, 25, 5]
for i in range(1, len(heap) - 1):
    delete(heap, length)
    length -= 1
print("Sorted heap => ", heap)
