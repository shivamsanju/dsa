# Insert 40 into -> [0, 30, 20, 15, 5, 10, 12, 6]
"""
Node at index i (i starts from 1, index 0 of a heap array is left unused)
----------------
Left child -> 2 * i
Right child -> 2 * i + 1
"""


def insert(arr: list[int], val: int):
    # Step 1: Insert the value at last
    arr.append(val)

    # Step 2: Swap with parent until parent is smaller (parent = i/2)
    i = len(arr) - 1
    while i > 1 and arr[i // 2] < arr[i]:
        arr[i], arr[i // 2] = arr[i // 2], arr[i]
        i = i // 2


heap = [0, 30, 20, 15, 5, 10, 12, 6]
insert(heap, 40)
print("New heap => ", heap)


# Create a heap from arr -> [5,12,10,30,6,25,15]
initial_heap = [0]
elements = [5, 12, 10, 30, 40, 6, 25, 15]
for elem in elements:
    insert(initial_heap, elem)

print("Created heap => ", initial_heap)
