def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0

    if x < arr[0]:
        return iterations, arr[0]
    elif x > arr[-1]:
        return iterations, arr[-1]

    while low <= high:

        mid = (high + low) // 2
        iterations += 1

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return iterations, arr[mid]

    if high < 0:
        return iterations, None
    else:
        return iterations, arr[low] if low < len(arr) else None

# Створюємо відсортований масив з дробовими числами та перевіряємо алгоритм на двох різних значеннях

arr = [2.1, 3, 4.3, 10.5, 40.7]
x = 42
y = 0

iterations, upper_bound = binary_search(arr, x)

print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)

iterations, upper_bound = binary_search(arr, y)

print("\nКількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)