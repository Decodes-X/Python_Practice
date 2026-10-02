import random

arr = [random.randint(1, 100) for _ in range(10)]
print("Unsorted array:", arr)

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)
