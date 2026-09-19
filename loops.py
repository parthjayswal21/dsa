#1. Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

#2. Print numbers from 10 to 1 using a while loop.
i = 10
while i > 0:
    print(i)
    i -= 1

#3. Print the multiplication table of a number.
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#4. Find the sum of numbers from 1 to n.
n = 10
print(sum(range(1, n + 1)))

#5. Find the factorial of a number.
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

#6. Print all even numbers between 1 and 100.
for i in range(2, 101, 2):
    print(i)

#7. Reverse a number using a loop.
n = 12345
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)

#8. Count the digits of a number.
n = 12345
print(len(str(n)))

#9. Check whether a number is prime.
n = 11
is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print("Prime" if is_prime else "Not Prime")

#10. Print Fibonacci series up to n terms.
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
