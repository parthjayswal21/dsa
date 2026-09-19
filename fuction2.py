# 11. Function to find the maximum of three numbers
def maximum_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# 12. Function to count vowels in a string
def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count

# 13. Function to reverse a string
def reverse_string(text):
    return text[::-1]
     

# 14. Function to check whether a string is a palindrome
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

# 15. Function to find the sum of all elements in a list
def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 16. Function to find the largest element in a list
def largest_element(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

# 17. Function to remove duplicate elements from a list
def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

# 18. Function to count how many times an element appears in a list
def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1

    return count

 
# 19. Function to check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# 20. Function to return all prime numbers between two numbers
def primes_between(start, end):
    primes = []

    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)

    return primes


print(maximum_three(10, 25, 15))
print(count_vowels("Hello World"))
print(reverse_string("Python"))
print(is_palindrome("madam"))
print(list_sum([10, 20, 30, 40]))
print(largest_element([10, 50, 20, 40]))
print(remove_duplicates([1, 2, 2, 3, 3, 4]))
print(count_element([1, 2, 2, 3, 2], 2))
print(is_prime(17))
print(primes_between(1, 20))
