# 21. Function to calculate Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# 22. Function to find the second-largest number in a list

def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

# 23. Function to sort a list without using sort()
def sort_list(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

# 24. Function to merge two lists and remove duplicates
def merge_lists(list1, list2):
    result = []

    for item in list1:
        if item not in result:
            result.append(item)

    for item in list2:
        if item not in result:
            result.append(item)

    return result










fibonacci(10)

numbers = [10, 20, 5, 30, 25]

print("Second largest:", second_largest(numbers))
print(sort_list([5, 2, 8, 1, 3]))

print(merge_lists([1, 2, 3], [3, 4, 5, 2]))
