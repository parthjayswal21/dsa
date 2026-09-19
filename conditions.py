
#1. Check whether a number is positive, negative, or zero.
n = -5
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#2. Check whether a person is eligible to vote.
age = 20
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

#3. Find the largest of three numbers.
a, b, c = 10, 25, 15
print(max(a, b, c))

#4. Check whether a year is a leap year.
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#5. Create a grade system based on marks.
marks = 82
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


#6. Check whether a number is divisible by 5 and 11.
n = 55
if n % 5 == 0 and n % 11 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")


#7. Create a simple calculator using if-elif-else.
a, b, op = 10, 5, '+'
if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/': print(a / b)
