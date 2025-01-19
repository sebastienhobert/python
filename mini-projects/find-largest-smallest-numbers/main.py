def find_largest_smallest(numbers):
    if not numbers:
        return None, None
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers  separated by spaces: ").split()))
    largest, smallest = find_largest_smallest(numbers)

    if largest is not None and smallest is not None:
        print(f"The largest number is: {largest}")
        print(f"The smallest number is: {smallest}")
    else:
        print("The list is empty")