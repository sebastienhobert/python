def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
        # the loop starts with j at 0
        # n is the length of the list to be sorted
        # i is the current iteration of the outer loop
        # by subtracting 1, we adjust the range to avoid comparing the last element[..]
        # the loop ends before reaching n - i - 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    sorted_numbers = bubble_sort(numbers)
    print("Sorted list:", sorted_numbers)