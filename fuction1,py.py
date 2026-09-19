#1 Write a function to print "Hello, World!".
def hello_world():
    print("Hello, World!")

# 2. Function that takes a name and prints a greeting
def greet(name):
    print("Hello,", name)

# 3. Function to add two numbers
def add(a, b):
    return a + b


# 4. Function to find the square of a number
def square(n):
    return n * n

# 5. Function to check whether a number is even or odd
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# 6. Function to find the maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

# 7. Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 8. Function to calculate the area of a circle
def circle_area(radius):
    return 3.14 * radius * radius

# 9. Function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# 10. Function to check whether a number is positive, negative, or zero
def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")


hello_world()
greet("Parth")
print(add(10, 20))
print(square(5))
even_odd(7)
print(maximum(10, 25))
print(celsius_to_fahrenheit(25))
print(circle_area(5))
print(factorial(5))
check_number(-10)
